from django.shortcuts import render
from .models import Blog 

# Create your views her
def blog_view(request,*args,**kwargs):
    # objec = Blog.objects.get(id)
    context = {"object"  : objec} 
    template_naam = "blog_view.html"
    
    return render(request,template_naam,context)