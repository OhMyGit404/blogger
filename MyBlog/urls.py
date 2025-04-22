from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('admin/', admin.site.urls),
]
