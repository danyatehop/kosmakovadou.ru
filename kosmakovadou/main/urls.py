"""kosmakovadou URL Configuration

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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('developments/', views.developments, name='developments'),
    path('news/', views.news, name='news'),
    path('article/<int:article_id>', views.page_arlicle, name='page'),
    path('develop/<int:develop_id>', views.page_develop, name='page'),
    path('feedback/', views.feedback, name="feedback"),
    path('section/<int:section_id>', views.section, name="section"),
    path('section/page/<int:page_id>', views.page, name="page"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
