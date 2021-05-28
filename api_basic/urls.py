from django.urls import path
from .views import ArticleDetailsApi, ArticleAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('article_details/<int:pk>/', ArticleDetailsApi.as_view()),
]
