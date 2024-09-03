
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/customer/', include('App_Auth.urls')),
    # path('api/admin_panel/', include('admin_panel.urls')),
]
