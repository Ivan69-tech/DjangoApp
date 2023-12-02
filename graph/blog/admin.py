from django.contrib import admin
from .models import Post, Contact, ExcelFile

# Register your models here.

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(ExcelFile)