"""programstatement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from std.views import (
    Import_view,
	simple_upload_Students,
    simple_upload_Schools,
    simple_upload_Books,
	student_details_search_view,
	student_details_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Import_view),
    path('student/',simple_upload_Students),
    path('school/',simple_upload_Schools),
    path('book/',simple_upload_Books),
    path('search/', student_details_search_view),
    path('search/<int:std_id> <str:std_name>/', student_details_view),
]
