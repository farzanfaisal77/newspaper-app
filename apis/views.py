from django.shortcuts import render
from rest_framework import generics
from accounts.models import CustomUser
from articles.models import Comment
from articles.models import Article
from .serializers import UserSerializer,ArticleSerializer,CommentSerializer
# Create your views here.

class UserList(generics.ListCreateAPIView):
    permission_classes=
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
class ArticleList(generics.ListCreateAPIView):
    permission_classes=
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class CommentList(generics.ListCreateAPIView):
    permission_classes=
    serializer_class=CommentSerializer
    #queryset=Comment.objects.all() = cant use cuz nested url doesnt know which one to use
    def get_queryset(self):
        return Comment.objects.filter(article_id=self.kwargs["article_pk"])
    
    
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
