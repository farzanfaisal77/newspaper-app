from .views import UserList,UserDetail,ArticleList,ArticleDetail,CommentList, CommentDetail
from django.urls import path


urlpatterns = [
    path("users/<int:pk>/",UserDetail.as_view(), name="user_detail"),
    path("users/",UserList.as_view(), name="user_list"),
    path("articles/<int:article_pk>/comments/<int:comment_pk>", CommentDetail.as_view(), name="comment_detail"),
    path("articles/<int:article_pk>/comments", CommentList.as_view(), name="comment_list"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
    path("articles/",ArticleList.as_view(), name="article_list"),
]
