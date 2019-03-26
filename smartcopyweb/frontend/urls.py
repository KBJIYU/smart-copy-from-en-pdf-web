from django.urls import include, path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('testapi/', test_api, name="testapi"),
    path('testhtml/', test_html, name="testhtml"),
    path('en/', smart_copy_en, name="en" )
]
