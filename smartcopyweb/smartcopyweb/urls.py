from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/', include('testapp.urls')),
    path('', include('frontend.urls')),
    # path('api/', include('smartapi.urls'))
]