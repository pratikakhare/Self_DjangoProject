from django.contrib import admin

# Register your models here.
from service.models import help, Card

class helpAdmin(admin.ModelAdmin):
    list_display = ('help_id','help_title','help_des')
admin.site.register(help,helpAdmin)
    
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_id','card_title','card_des')
admin.site.register(Card,CardAdmin)