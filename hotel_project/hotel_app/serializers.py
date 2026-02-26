from rest_framework import serializers
from .models import Country, City, Hotel, HotelImage, Room, RoomImage, UserProfile, Review, Booking, Service


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True, source='city_set')

    class Meta:
        model = Country
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(many=True, read_only=True, source='hotellistimage_set')
    countries = CountrySerializer(many=True, read_only=True, source='country_set')
    cities = CitySerializer(many=True, read_only=True, source='city_set')

    class Meta:
        model = Hotel
        fields = ['id','hotel_name','city','country','images']

class HotelDetailSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(many=True, read_only=True, source='hoteldetailimage_set')

    class Meta:
        model = Hotel
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True, source='roomimage_set')

    class Meta:
        model = Room
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ServiceProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'