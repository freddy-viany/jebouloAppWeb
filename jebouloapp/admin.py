from django.contrib import admin

from .models import CustomerModel,AnnounceModel

admin.site.register(CustomerModel)
admin.site.register(AnnounceModel)

# Register your models here.
