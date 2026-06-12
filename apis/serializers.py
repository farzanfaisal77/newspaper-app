from rest_framework import serializers
from accounts.models import CustomUser
from articles.models import Comment
from articles.models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("id", "username", "email", "age",)
    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=("id", "author", "title", "body", "date")
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=("id", "author", "article", "comment")