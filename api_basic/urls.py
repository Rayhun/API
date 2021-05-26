from django.urls import path
from .views import article_list, article_detaile
urlpatterns = [
    path('article/', article_list),
    path('article_details/<int:pk>/', article_detaile),
]
