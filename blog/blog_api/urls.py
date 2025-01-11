from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.api_categories),
    path('categories/<int:pk>/', views.api_category_detail),
    path('home/slider/', views.api_home_slider),
    path('faq/', views.api_faq),
    path('faq/<int:pk>/', views.api_faq_detail)
]