from django.contrib import admin
from .models import Destination,Profile,Entertainment,Order

# Register your models here.

admin.site.register(Profile)
admin.site.register(Destination)
admin.site.register(Entertainment)
admin.site.register(Order)