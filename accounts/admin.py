from django.contrib import admin
from .models import CustomUser, State, City

admin.site.register(CustomUser)
admin.site.register(State)
admin.site.register(City)