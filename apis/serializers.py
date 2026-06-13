from rest_framework import serializers
from accounts.models import CustomUser
from articles.models import Comment
from articles.models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("id", "username", "email", "age",)
    
class ArticleSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=Article
        fields=("id", "author", "title", "body", "date")
        
class CommentSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    article=serializers.ReadOnlyField(source='article.id')
    class Meta:
        model=Comment
        fields=("id", "author", "article", "comment")