"""core URL Configuration

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
from blog.admin import blog_site
from bookstore.admin import bookstore_site

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin2/', blog_site.urls),
    path('admin3/', bookstore_site.urls),
]

#to serve the static within the local developement
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#TODO You can add this to your setup.sh file
admin.site.index_title = "The book Store"
admin.site.site_header = "The Book Store Admin"
admin.site.site_title = "Site Title Book Store"
