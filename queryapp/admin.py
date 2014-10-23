from django.contrib import admin

# Register your models here.
from django.contrib import admin
from queryapp.models import Question

admin.site.register(Question)