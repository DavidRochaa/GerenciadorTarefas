from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from tarefas import views as tarefas_views

#Redireciona para a página de login
def redirect_to_login(request):
    return redirect('login')

#Mapeamento das URLS 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tarefas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', tarefas_views.signup, name='signup'),
    path('tarefas/', include('tarefas.urls')),
]
