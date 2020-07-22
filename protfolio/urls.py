"""protfolio URL Configuration

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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from projects import views as projectsView
from accounts import views as accountsView

urlpatterns = [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        accountsView.activate, name='activate'),
    path('admin/', admin.site.urls, name='admin'),
    path('', projectsView.homePage, name='homePage'),
    path('home', projectsView.homePage, name='homePage'),
    path('login', accountsView.loginPage, name='loginPage'),
    path('logout', accountsView.logoutUser, name='logoutUser'),
    path('register', accountsView.registerPage, name='registerPage'),
    path('projects/<int:project_id>',
         projectsView.detailPage, name='detailPage'),
    path('projects/create', projectsView.createPage, name='createPage'),
    path('projects/<int:project_id>/edit',
         projectsView.editPage, name='editPage'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
