"""
URL configuration for GigaStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/",include('shop.urls'), name="shop_index"),
    path("blog/",include('blog.urls'), name="blog_index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
This line appends a route for serving media files (such as images) during development.
settings.MEDIA_URL defines the base URL for media files (e.g., /media/).
settings.MEDIA_ROOT defines the file system directory where media files are stored.
This ensures that files uploaded through models using ImageField or FileField can be accessed via a URL in development (e.g., localhost:8000/media/yourfile.jpg).

"""




