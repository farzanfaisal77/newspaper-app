from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        email_template_name='registration/password_reset_email.html',
        html_email_template_name='registration/password_reset_email.html'
    ), name='password_reset'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("articles/", include("articles.urls")),
    path("apis/", include("apis.urls")),
    path("", include("pages.urls")),
]
