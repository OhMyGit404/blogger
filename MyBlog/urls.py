from django.urls import path
from . import views
from .views import PostListView, PostDetailView
from django.contrib import admin
urlpatterns = [
    path('',PostListView.as_view(), name='index'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('about/',views.about, name='about'),
    path('admin/', admin.site.urls),
]
