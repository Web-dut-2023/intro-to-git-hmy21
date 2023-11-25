from django.contrib import admin
from .models import Train, Station, Passenger
#管理界面都有些啥？
class TrainAdmin(admin.ModelAdmin):
    list_display = ("trainNum", "origin", "destination", "duration", "cost")
class StationAdmin(admin.ModelAdmin):
    list_display = ("code", "city")
# Register your models here.
class PassengerAdmin(admin.ModelAdmin):
    list_display = ("first", "last", "contact")
admin.site.register(Train,TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Passenger, PassengerAdmin)