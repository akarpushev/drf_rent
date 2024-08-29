from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike', 'status')
    search_fields = ('bike', 'status')
    list_filter = ('status',)


# admin.site.register(Bike)
