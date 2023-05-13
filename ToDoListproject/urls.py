"""ToDoListproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ToDoListapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainPage),
    path('Main',views.mainPage,name='mainPage'),
    path('formData',views.formPage,name='formData'),
    path('update/<id>',views.updatePage,name='update'),
    path('delete/<id>',views.deletePage,name='delete')
]
