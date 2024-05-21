from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer,CommentSerializer
from .models import Article,Comment
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated 
# Create your views here.

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
            articles = get_list_or_404(Article)
            serializer = ArticleListSerializer(articles, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                # serializer.save()
                serializer.save(user=request.user)
                request.user.points = request.user.points + 30
                request.user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'DELETE' and request.user == article.user and request.user.points >= 30 :
        request.user.points = request.user.points - 30
        request.user.save()
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data,partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def comment_list(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = Comment.objects.filter(article=article)
    if request.method == 'GET':
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request.user.points = request.user.points + 5
            request.user.save()
            serializer.save(article=article,user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE','PUT'])
def comment_detail(request,article_pk,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE' and request.user == comment.user and request.user.points >= 5:
        comment.delete()
        request.user.points = request.user.points - 5
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT' and request.user == comment.user:
        serializer = CommentSerializer(comment, data=request.data,partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)