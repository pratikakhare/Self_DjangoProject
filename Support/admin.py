from django.contrib import admin
from Support.models import SupportDesk
# Register your models here.

class SupportAdmin(admin.ModelAdmin):
    list_display = ('support_name','support_email','support_date','support_time')
admin.site.register(SupportDesk,SupportAdmin)
