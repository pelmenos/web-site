from django.contrib import admin
from . import models


class PetAdmin(admin.ModelAdmin):
    list_display = ['breed', 'id']


admin.site.register(models.Cat, PetAdmin)
admin.site.register(models.Dog, PetAdmin)
admin.site.register(models.Sex)
admin.site.register(models.Team)
admin.site.register(models.Breed_cat)
admin.site.register(models.Breed_dog)
