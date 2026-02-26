from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

from .views import (
    CountryViewSet,
    CityViewSet,
    RoomViewSet,
    UserProfileViewSet,
    ReviewViewSet,
    BookingViewSet,
    RoomImageViewSet,
    HotelListView,
    HotelDetailView
)

router = DefaultRouter()
router.register('countries', CountryViewSet)
router.register('cities', CityViewSet)
router.register('rooms', RoomViewSet, basename='room')
router.register('room-images', RoomImageViewSet, basename='room-image')
router.register('users', UserProfileViewSet)
router.register('reviews', ReviewViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
