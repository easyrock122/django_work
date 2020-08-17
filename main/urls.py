from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('introduce/', views.introduce, name = "introduce"),
    path('profile/<int:designer_id>/', views.detail, name = "detail"),
    path('new/', views.new, name="new" ),
    path('create/', views.create, name="create"),
    path('delete/<int:designer_id>/', views.delete, name='delete'),
    path('update/<int:designer_id>/', views.update, name = "update"),
]