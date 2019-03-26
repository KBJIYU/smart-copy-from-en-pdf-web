from django.urls import include, path
from .views import *

app_name = 'testapp'

urlpatterns = [
    path('testapi/', test_api, name="testapi"),
    path('testhtml/', test_html, name="testhtml")
]
