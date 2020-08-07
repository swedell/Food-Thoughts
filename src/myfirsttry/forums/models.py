from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings  
from django.urls import reverse
from comments.models import Comment

User = settings.AUTH_USER_MODEL 

# Create your models here.
class ForumPost(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    topic = models.CharField(max_length = 150)
    category = models.CharField(max_length = 50)
    message = models.TextField()
    slug = models.SlugField(blank = True, null=True)
    # message_timings = models.DateTimeField(auto_now_add=True)   //replaced by timestamp
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    
    
#---------------these are subclasses-----------------

    class Meta:
        ordering = ['-updated','-timestamp']


#-----------------these are methods----------------

    def get_absolute_url(self):
        return reverse('forums:detail', kwargs={"slug" : self.slug})

    def __str__(self):
        return self.topic

#-----------these are properties----------------

    @property 
    def title(self):
        return(self.topic)
    
    @property
    def get_comments(self):
        qs = Comment.objects.filter_by_instance(self)
        return qs 

    @property
    def get_content_type(self):
        instance = selfcontent_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

#-----------------these are signals-------------

def fo_pre_save_reciever(sender,instance,*args,**kwargs):
    # print("saving...")
    # print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def fo_post_save_reciever(sender,instance,created,*args,**kwargs):
    # print("saved")
    # print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

pre_save.connect(fo_pre_save_reciever,sender=ForumPost)
post_save.connect(fo_post_save_reciever,sender=ForumPost)