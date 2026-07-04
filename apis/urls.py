from .views import UserList,UserDetail,ArticleList,ArticleDetail,CommentList, CommentDetail,HomeView
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="api_schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="api_schema")),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="api_schema")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("users/<int:pk>/",UserDetail.as_view(), name="api_user_detail"),
    path("users/",UserList.as_view(), name="api_user_list"),
    path("articles/<int:article_pk>/comments/<int:comment_pk>/", CommentDetail.as_view(), name="api_comment_detail"),
    path("articles/<int:article_pk>/comments/", CommentList.as_view(), name="api_comment_list"),
    path("articles/<int:pk>/", ArticleDetail.as_view(), name="api_article_detail"),
    path("articles/",ArticleList.as_view(), name="api_article_list"),
    path("", HomeView.as_view(), name="api_apihome")
]
