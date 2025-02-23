"""
URL configuration for crudapi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from crudapi_app import views
from crudoperation import views
from authentication_with_email import views as user_view
from django.contrib.auth import views as auth
from todolist import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crudapi/',include('crudapi_app.urls')),
    path('crudope/',include('crudoperation.urls')),
    # '''# authentication_with_email related urls...
    # path('', include('authentication_with_email.urls')),  # Include app-level URLs for user app
    # path('login/', user_view.Login, name='login'),
    # path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    # path('register/', user_view.register, name='register'),'''
    path('',include('todolist.urls'))
 ]
