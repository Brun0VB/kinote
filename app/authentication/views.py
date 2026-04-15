from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, "authentication/index.html")


User = get_user_model()


class CustomLoginView(LoginView):
    """
    Usa a LoginView do próprio Django — segura e já testada.
    Só precisamos apontar o template.
    """
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True  # redireciona quem já está logado


class RegisterView(CreateView):
    """View de registro de novo usuário."""
    model = User
    form_class = CustomUserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('authentication:login')

    def dispatch(self, request, *args, **kwargs):
        """Redireciona usuário autenticado para o dashboard."""
        if request.user.is_authenticated:
            return redirect('authentication:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def logout_view(request):
    """Logout via POST — boa prática de segurança (evita CSRF)."""
    if request.method == 'POST':
        logout(request)
    return redirect('authentication:login')


# @login_required
# def dashboard(request):
#     """Área protegida — só acessível para usuários autenticados."""
#     return render(request, 'authentication/dashboard.html', {
#         'user': request.user
#     })