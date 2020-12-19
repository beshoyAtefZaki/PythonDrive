"""MyDrive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from userprofile.views import ( login_page , 
								register_page,
								home_page,
								validate_username ,
								profile_page,
								validate_pass,
								logout_view)

from fileapp.views import user_files,validate,create_file,serch_in_files
from django.conf.urls.static import static

from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:idx>', profile_page, name='profile'),
    path('register/', register_page, name='register'),
    path('validate/' , validate_username , name='validate'),
    path('v_pass/' ,validate_pass , name='v_pass'),
    path('u_files/<int:idx>/',user_files, name="files"),
    path('validate_files/',validate, name="validate_files"),
    path('create_file/',create_file, name="create_file"),
    path('search/' ,serch_in_files , name="search" ),

    path('', home_page, name='home')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
