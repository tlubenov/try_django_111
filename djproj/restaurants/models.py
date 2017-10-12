#import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
#    my_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)

#    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    slug = models.SlugField(null=True, blank=True)#unique=True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
#        return "/restaurants/{self.slug}"
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(RestaurantLocation, self).save(*args, **kwargs)
        else:
            print ('Object already exists')

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print ('saving ...')
    print (instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()




#def rl_post_save_receiver(sender, instance, *args, **kwargs):
#    print ('saved')
#    print (instance.timestamp)
##    if not instance.slug:
##        instance.slug = unique_slug_generator(instance)
##        instance.save()


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

#pre_save.connect(rl_post_save_receiver, sender=RestaurantLocation)