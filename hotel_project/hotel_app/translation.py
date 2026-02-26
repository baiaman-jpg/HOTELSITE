from modeltranslation.translator import register, TranslationOptions
from .models import Country, City, Hotel, Room

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', )

@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)
