
import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocation


def restaurant_listview(req):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(req, template_name, context)

# complete Restaurant List View including search by Category
class RestaurantListView(ListView):
    # named template_name
    template_name = 'restaurants/restaurants_list.html'

    # if name template to model name + _list than can completely remove the template_name var

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


# end of change


class RestaurantDetailView(DetailView):
    # get all database objects and find feature one
    queryset = RestaurantLocation.objects.all()

    # get only matching object from the database
#    queryset = RestaurantLocation.objects.get(slug=kwargs.get("slug"))


    # named template_name
    template_name = 'restaurants/restaurants_details.html'

    # if name template to model name + _list than can completely remove the template_name var

    def get_context_data(self, *args, **kwargs):
        print (self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        return context

#    def get_object(self, *args, **kwargs):
#        rest_id = self.kwargs.get('rest_id')
#        object = get_object_or_404(RestaurantLocation, uuid=rest_id) # pk for rest_id
#        return object





from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
#        obj = RestaurantLocation.objects.create(
#            name = form.cleaned_data.get('name'),
#            location = form.cleaned_data.get('location'),
#            category = form.cleaned_data.get('category')
#        )
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/form123.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


#@login_required(login_url='/login/')
class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/form123.html'
#    success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context




# these are for training

class MexicanRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
    template_name = 'restaurants/restaurants_list.html'

class AsianFusionRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')
    template_name = 'restaurants/restaurants_list.html'

# flexible query sets
class SearchRestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        print (self.kwargs)
        slug = self.kwargs.get('slug')
        print (slug)
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


#def home(request):
#    # this is not supported by Python 3.5
#    html_var = 'html vars'
#    html_ = f"""
#        <html>
#        <head>
#        </head>
#        <body>
#        hello
#        <h1>{html_var}</h1>
#        </body>
#        </html>
#    """
#    return HttpResponse(html_)


class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        num = random.randint(0, 10000)
        context = {
            'page_title': 'Home Page',
            'page_header': 'This is a header',
            'uid': num,
        }
        #print (context)
        return context








class MapView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        context = {}
        return render(request, 'map.html', context)

#    def post(self, request, *args, **kwargs):
#        print(kwargs)
#        context = {}
#        return render(request, 'map.html', context)

#    def put(self, request, *args, **kwargs):
#        print(kwargs)
#        context = {}
#        return render(request, 'map.html', context)

