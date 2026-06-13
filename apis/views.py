from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly
from accounts.models import CustomUser
from articles.models import Comment
from articles.models import Article
from .serializers import UserSerializer,ArticleSerializer,CommentSerializer
from .permissions import IsAuthorElseRead,RWifAuthenticated
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name="apihome.html"

class UserList(generics.ListCreateAPIView):
    permission_classes=[IsAdminUser]
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminUser]
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
class ArticleList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly | IsAdminUser]
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
    
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthorElseRead | IsAdminUser]
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
class CommentList(generics.ListCreateAPIView):
    permission_classes=[RWifAuthenticated | IsAdminUser]
    serializer_class=CommentSerializer
    #queryset=Comment.objects.all() = cant use cuz nested url doesnt know which one to use
    def get_queryset(self):
        return Comment.objects.filter(article_id=self.kwargs["article_pk"])
    def perform_create(self,serializer):
        serializer.save(author=self.request.user,article_id=self.kwargs["article_pk"])
    
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[RWifAuthenticated | IsAdminUser]
    serializer_class=CommentSerializer
    def get_object(self):
        obj= Comment.objects.get(
            article_id=self.kwargs['article_pk'],
            id=self.kwargs['comment_pk']
        )
        self.check_object_permissions(self.request,obj)
        return obj
    
