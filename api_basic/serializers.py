from rest_framework import serializers
from .models import Article


class ArticleSerializers(serializers.Serializer):
    """ Article Serializer """
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()

    def create(self, validated_data):
        """ Article Create """

        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        """ Article Update  """

        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
