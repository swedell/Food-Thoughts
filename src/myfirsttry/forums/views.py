from urllib.parse import urlparse

# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from django.contrib.contenttypes.models import ContentType

from django.db.models import Q
# from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
#                               render)
# from django.utils.http import urlencode
# from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from comments.models import Comment
from comments.forms import CommentForm  

from .forms import ForumPostModelForm
from .models import ForumPost
from django.urls import reverse
from django.http import HttpResponseForbidden

# from comments.models import Comment

all_cat_raw = ForumPost.objects.order_by('category').values_list('category',flat=True).distinct()
all_cat = [urlparse(cat).geturl() for cat in all_cat_raw]



class ForumPostCreateView(LoginRequiredMixin, CreateView):
    form_class = ForumPostModelForm
    login_url = '/login/'
    template_name = "forums/form.html" 
    # success_url = "/forum/"
    

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ForumPostCreateView,self).form_valid(form)


class HomeView(ListView):
    # def get_context_data(self,*args,**kwargs):
    #     context = super(HomeView,self).get_context_data(*args,**kwargs)
    #     all_obj = ForumPost.objects.all().order_by('-timestamp')
    #     # .filter(topic__icontains = 'c')
    #     #for sorting message by latest and from topic containing c 
    #     list_of_obj = list(all_obj)

    #     print(all_cat)
    #     context = {
    #     "list_of_object": list_of_obj,
    #     "list_of_categories": all_cat}
    #     return context
                                        
    queryset = ForumPost.objects.all().order_by('-timestamp')

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_categories']= all_cat 
        return context

class CategoryView(ListView):
    # def get_context_data(self,*args,**kwargs):
        
    #     all_obj = get_list_or_404( ForumPost,category__icontains = kwargs['category'])
    #     list_of_obj = all_obj

    #     context = {
    #         "list_of_object":list_of_obj,
    #         "list_of_categories": all_cat
        
    #                         }
    #     return context

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category :
            queryset = ForumPost.objects.filter(
                Q(category__iexact = category) |
                Q(category__icontains= category)  
                )
        else:
            queryset = ForumPost.objects.none()
        return queryset

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_categories']= all_cat 
        return context


class ForumPostDetailView(FormMixin,DetailView):
    model = ForumPost  
    form_class = CommentForm
    
    def get_initial(self):
        instance = self.get_object()
        initial_data = {
            "object_id": instance.id,
            "content_type": instance.get_content_type.id
        }
        return initial_data

    def get_success_url(self):
        return reverse('forums:detail',kwargs={'slug':self.object.slug})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()

        comment_form = self.get_form()

        if comment_form.is_valid():
            return self.form_valid(comment_form)

        else:
            return self.form_invalid(comment_form)

    def form_valid(self, form):
        input_content_type = form.cleaned_data.get("content_type")
        print(input_content_type)
        content_type = ContentType.objects.get(id=input_content_type)

        obj_id = form.cleaned_data.get('object_id')

        content_data = form.cleaned_data.get("content")


        new_comment, created = Comment.objects.get_or_create(user = self.request.user,content_type= content_type,object_id = obj_id,content = content_data)
						
        return super().form_valid(form)
        

        


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_categories'] = all_cat
    
        # instance = self.get_object()

        # cont_type = ContentType.objects.get_for_model(ForumPost)
        # # print(self.get_object().id)
        # obj_id = self.get_object().id

        # comments = Comment.objects.filter_by_instance(instance)
        # context['comments'] = comments  

    # context['comments'] = Comment.objects.filter(forum=context.get('object'))
    # print(context)


 
        # obj = get_object_or_404(ForumPost, slug=kwargs['slug'])
        # print(obj)
        # context = {
        #     "object" : obj,
        #     "list_of_categories": all_cat

        #         }
            
    #     print(args,kwargs)
        # print("Djando does",request.method,request.path,request.user)
        
        return context


#-----------------------------------------------------------------
# Create your views here.
#CRUD




            
# def list_view(request,*args,**kwargs):
    
#     all_obj = ForumPost.objects.all().order_by('-timestamp')
#     # .filter(topic__icontains = 'c')
# #for sorting message by latest and from topic containing c 
#     list_of_obj = list(all_obj)

#     print(all_cat)
#     context = {
#         "list_of_object": list_of_obj,
#         "list_of_categories": all_cat
#     }

#     return render(request, "forums/index.html",context)


# Create your views here.
# def category_view(request,*args,**kwargs):

    
#     all_obj = get_list_or_404( ForumPost,category__icontains = kwargs['category'])
#     list_of_obj = all_obj

#     context = {
#         "list_of_object":list_of_obj,
#         "list_of_categories": all_cat
        
#     }
     
    
#     return render(request, "forums/index.html",context)


# Create your views here.
# def detail_view(request,*args,**kwargs):
    
#     obj = get_object_or_404(ForumPost, slug=kwargs['slug'])
#     print(obj)
#     context = {
#         "object" : obj,
#         "list_of_categories": all_cat

#     }
    
#     print(args,kwargs)
#     print("Djando does",request.method,request.path,request.user)
    
#     return render(request, "forums/detail.html",context)
# #CRUD 
# def forumpost_retrieve_view(request,*args,**kwargs):


# def forumpost_update_view(request,*args,**kwargs):
# def forumpost_create_view(request,*args,**kwargs):
#     cotext ={'form':None}
#     return render(request,forum/create.html,context)
# def forumpost_delete_view(request,*args,**kwargs):

#just a dummy 
# def contact_view(request,*args,**kwargs):
    
    
#     context = {
        
#     } 

# class ContactView(TemplateView):
#     template_name = 'contact.html'

#     def get_context_data(self,*args,**kwargs):
#         context = super(ContactView,self).get_context_data(*args,**kwargs)
#         print(context)
#         return context

    
# class ContactTemplateView(TemplateView):
#     template_name = 'contact.html'

#------------------------------------------------------------------------



# @login_required()#login_url = '/login/'
# def forumpost_createview(request):
#     template_name = "forums/form.html"
#     form = ForumPostModelForm(request.POST or None)
#     error = None
#     if form.is_valid():
#         print('abhi wala user',request.user.is_authenticated)
#         if request.user.is_authenticated:
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
            
#             # obj = ForumPost.objects.create(**form.cleaned_data)
#             # obj = form.save(commit=False)
#             # obj.topic = form.cleaned_data.get("topic") 
#             # obj.save()

#             form = ForumPostModelForm()
            
#             return redirect('/forum/')
#         else:
#             return redirect('/login/')
#     else:
#         error = form.errors
#     context ={"form" : form, "error":error}
#     return render(request, template_name,context)
