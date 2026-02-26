from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


class Country(models.Model):
    country_name = models.CharField(max_length=100,unique=True)
    country_image = models.ImageField(upload_to="country_image/",blank=True,null=True)
    def __str__(self):
        return self.country_name

class UserProfile(AbstractUser):
    pass
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(13), MaxValueValidator(80) ], null=True, blank=True)
    user_image = models.ImageField(upload_to='user_image/', null=True, blank=True)
    phone_number = PhoneNumberField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    RoleChoices = (
        ('owner',  'owner',),
        ('client', 'client', )
    )
    role = models.CharField(max_length=100, choices=RoleChoices ,default='client')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}{self.role}'

class City(models.Model):
    city_name = models.CharField(max_length=100,unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_image = models.ImageField(upload_to='city_image/', null=True, blank=True)

    def __str__(self):
        return self.city_name

class Service(models.Model):
    service_name = models.CharField(max_length=100,unique=True)
    service_image = models.ImageField(upload_to='service_image/', null=True, blank=True)
    def __str__(self):
        return self.service_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100,unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    postal_code = models.PositiveIntegerField()
    street_address = models.CharField(max_length=100)
    hotel_stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(13), MaxValueValidator(80)])
    hotel_description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.hotel_name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image/', null=True, blank=True)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    Type_Choices = (
        ('люкс', 'люкс',),
        ('вип', 'вип'),
        ('бизнес', 'бизнес',),
        ('эконом', 'эконом',),
        ('семейный', 'семейный',),
    )
    type = models.CharField(max_length=100 , choices=Type_Choices)
    Status_Choices = (
    ('Занято','Занято'),
    ('В уборке', 'В уборке'),
    ('Свободный ', 'Свободный')
    )
    status_room = models.CharField(max_length=100,choices=Status_Choices)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    room_description = models.TextField()

    def __str__(self):
        return self.rooom_number

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image/', null=True, blank=True)


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField( blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(choices= [(i, str (i)) for i in range(1,11)], null=True ,blank=True)
    def __str__(self):
        return f'{self.rating} {self.hotel.hotel_name}{self.user.username}'


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.hotel}{self.user}{self.room}'