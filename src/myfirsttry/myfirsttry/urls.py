"""myfirsttry URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import include, path, re_path

from pages.views import contact_view, feedback_view, home_view
from products.views import product_detail_view

    # from pages import views




urlpatterns = [
    #for forum
    path('forums/',include('forums.urls',namespace="forums")),   # forums:home
    path('admin/', admin.site.urls),
    path('', home_view),


    path('login/',LoginView.as_view(),name = "login"),
    path('logout/',LogoutView.as_view(),name = "logout"),
    # path('logout/',LogoutView.as_view(),name = "logout"),
    path('password-reset/',PasswordResetView.as_view(),name = "password_reset"),



    re_path(r'^contacts?/$', contact_view),
    path('feedback/', feedback_view),
    path('detail/',product_detail_view),


]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
