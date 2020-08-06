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



# from pages import views
# from pages.views import contact_view, feedback_view, home_view
# from products.views import product_detail_view
# from .views import detail_view,category_view,list_view
# from .views import  ListView ,CategoryView, DetailView
# from django.contrib.auth.views import LoginView

from django.urls import path
from django.views.generic import TemplateView

from .views import (CategoryView, ForumPostCreateView, ForumPostDetailView,
                    HomeView)

app_name = 'forums'

urlpatterns = [
    path('',HomeView.as_view(template_name='forums/forumpost_list_index.html'), name = "homepage"),
    path('create-forum/',ForumPostCreateView.as_view(),name = "create"),
    path('c/<str:category>/',CategoryView.as_view(template_name='forums/forumpost_list.html'), name= "category"),  
    path('s/<slug:slug>/',ForumPostDetailView.as_view(template_name='forums/forumpost_detail.html'), name = "detail"),

    path('d/',TemplateView.as_view(template_name='forums/contact.html'),name = "contact"),


    # path('login/',LoginView.as_view())  #/forum//login/

    # path('about/',about_view),

]
