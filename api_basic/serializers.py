from rest_framework import serializers
from .models import Article


class ArticleSerializers(serializers.ModelSerializer):
    """ Article Serializer """
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']
