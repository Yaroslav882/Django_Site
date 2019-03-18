from django.contrib import admin
from django.urls import path

from home_page import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
]
