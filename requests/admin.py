from django.contrib import admin

from .models import Request

@admin.register(Request)
class RequestModelAdmin(admin.ModelAdmin):
    pass
