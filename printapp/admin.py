from django.contrib import admin
from printapp.models import PrintModel,Comment

# Register your models here.
admin.site.register(PrintModel)
admin.site.register(Comment)