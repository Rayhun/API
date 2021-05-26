from rest_framework import serializers
from .models import Article


class ArticleSerializers(serializers.Serializer):
    """ Article Serializer """
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    create_at = serializers.DateField(auto_now_add=True)
    update_at = serializers.DateField(auto_now=True)

    def create(self, validated_data):
        """ Article Create """

        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        """ Article Update  """

        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.email = validated_data.get("email", instance.email)
        instance.create_at = validated_data.get("create_at", instance.create_at)
        instance.update_at = validated_data.get("update_at", instance.update_at)
