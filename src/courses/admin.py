from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import course

class postAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'

admin.site.register(course,postAdmin)
