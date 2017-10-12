from .base import *
#from ..old_settings import *

from .production import *

try:
    from .local import *
except Exception as ex:
    print(ex)
    pass