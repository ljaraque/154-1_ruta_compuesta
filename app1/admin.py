from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('descripcion', 'rol', 'peso', 'altura', 'direccion')

admin.site.register(Profile, ProfileAdmin)