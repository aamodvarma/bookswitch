from django.contrib import admin
from .models import *
from functools import update_wrapper

from django.http import Http404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ShippingAddress)
