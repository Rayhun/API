from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http import response, JsonResponse
from .models import Article
from .serializers import ArticleSerializers

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializers(article, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def article_detaile(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return JsonResponse(status=400)

    if request.method == "GET":
        serializer = ArticleSerializers(article)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializers(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        article.delete()
        return JsonResponse(status=204)