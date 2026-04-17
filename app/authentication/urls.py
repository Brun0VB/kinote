from django.urls import path
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from . import views


app_name = "authentication"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html',
        success_url='/authentication/password-change/done/'
    ), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
    ), name='password_change_done'),
]