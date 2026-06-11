from rest_framework import serializers
from accounts.models import CustomUser
from articles.models import Comment
from articles.models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("id", "username", "email", "age",)