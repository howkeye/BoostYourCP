"""hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from profiles import views as p_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', p_views.register,name='register'),
    path('profile', p_views.profile,name='user_profile'),
    path('about/', p_views.profile,name='about'),
    path('login/',auth_views.LoginView.as_view(template_name='profiles/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='profiles/logout.html'),name='logout'),
    path('codechef/', p_views.codechef,name="codechef"),
    path('codeforce/', p_views.codeforce,name="codeforce"),
    path('send/', p_views.send_email,name="send_email"),
    path('home/', p_views.home,name="home"),
    path('', p_views.home),
    path('post/', p_views.create_post,name="create_post"),
    path('announcements/', p_views.announcements,name="Announcements"),
    path('contests/', p_views.contests,name="contests"),
    path('get_ratings/',p_views.getuser,name="get_ratings"),
    path('ratings/',p_views.ratings,name="ratings"),
    path('api_codechef', p_views.api_codechef),
    path('api_codeforce', p_views.api_codeforce)
]
