from django.urls import path

from .views import CarSearchView

urlpatterns = [
    path('search/', CarSearchView.as_view(), name='car_search'),
    # Add other URL patterns for your app if needed
]
