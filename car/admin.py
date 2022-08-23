from django.contrib import admin
from .models import *


# Register your models here.

#=======================================================================
@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
  pass


#=======================================================================
@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
  pass


#=======================================================================
@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
  pass


#=======================================================================
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
  pass


#=======================================================================
@admin.display(description='Vehicle')
def upper_case_name(obj):
    return ("%s %s %s" % (obj.year, obj.make, obj.model))

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
  list_display = (upper_case_name, 'color', 'vin', 'millage', 'price', )

