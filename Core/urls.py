
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin-login/', include('App_Auth.urls')),
    path('booking/', include('App_Hotel.urls')),
]
