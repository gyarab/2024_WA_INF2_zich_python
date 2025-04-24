from django.contrib import admin
from .models import EngineSpecifications, Category, Manufacturer

# Register your models here
admin.site.register(EngineSpecifications)
admin.site.register(Category)
admin.site.register(Manufacturer)