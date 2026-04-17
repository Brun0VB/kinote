from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # Troca de senha — views prontas do Django
    # path('password-change/', PasswordChangeView.as_view(
    #     template_name='accounts/password_change.html',
    #     success_url='/accounts/password-change/done/'
    # ), name='password_change'),
    # path('password-change/done/', PasswordChangeDoneView.as_view(
    #     template_name='accounts/password_change_done.html'
    # ), name='password_change_done'),
]