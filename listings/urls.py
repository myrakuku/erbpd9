from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listings, name='index'),
    # variable path, setted on 'views.py'
    path('<int:listing_id>', views.listing, name='listing'),
]