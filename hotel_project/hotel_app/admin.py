
from django.contrib import admin
from .models import Country, City, Hotel, HotelImage, Room, RoomImage, UserProfile


class CityInline(admin.TabularInline):
    model = City
    extra = 1

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]
    list_display = ('id', 'country_name')


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInline]
    list_display = ('id', 'hotel_name', 'city')


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]
    list_display = ('id', 'hotel', 'room_number')


admin.site.register(City)
admin.site.register(HotelImage)
admin.site.register(RoomImage)
admin.site.register(UserProfile)