from django.contrib import admin
from .models import Train, Station, Passenger

class TrainAdmin(admin.ModelAdmin):
    list_display = ("trainNum", "origin", "destination", "duration", "cost")
# Register your models here.
admin.site.register(Train,TrainAdmin)
admin.site.register(Station)
admin.site.register(Passenger)