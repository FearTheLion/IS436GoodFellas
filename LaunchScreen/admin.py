from django.contrib import admin

# Register your models here.

from .models import Interests, Major, Uni_Class

admin.site.register(Interests)
admin.site.register(Major)
admin.site.register(Uni_Class)