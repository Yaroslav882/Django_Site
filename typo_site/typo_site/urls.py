from django.contrib import admin
from django.urls import path, include

from home_page import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('signup/', views.signup, name='signup'),
    path('my_info/', views.my_info, name='my_info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
