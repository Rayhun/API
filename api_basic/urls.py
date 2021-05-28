from django.urls import path
from .views import article_detaile, ArticleAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('article_details/<int:pk>/', article_detaile),
]
