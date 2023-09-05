"""
URL configuration for project project.

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
from django.urls import path
from table.views import *
from vacancies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', main_table),
    path('vacancies/', main_vacancies),
    path('vacancies/edit/', edit_for_id),
    path('vacancies/edit_new/', new_edit_for_id),
    path('vacancies/create/', add_vacancies),
    path('vacancies/delete/', delete_vacancies),
    path('vacancies/card/', card),
    path('search/', main_search),
    path('search/all/', all_data),
    path('save/', redirect),
    path('test/', test)
]
