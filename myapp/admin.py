from django.contrib import admin
from .models import Service, Post, Appointment

admin.site.register([Service, Post, Appointment])

