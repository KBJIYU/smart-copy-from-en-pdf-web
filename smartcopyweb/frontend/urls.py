from django.urls import include, path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('en/', smart_copy_en, name="en" )
]
