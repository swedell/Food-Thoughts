from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType, ContentTypeManager

# from forums.models import ForumPost
# Create your models here.

class CommentManager(models.Manager):

    def all(self):
        qs = super(CommentManager,self).filter(parent = None)
        return qs

    def filter_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager,self).filter(content_type = content_type, object_id = obj_id).filter(parent=None)
        return qs


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Comment(models.Model):

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET(get_sentinel_user))
  
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField(max_length= 400)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    parent = models.ForeignKey("self",null = True, blank = True,on_delete=models.CASCADE)
    
    

    objects = CommentManager()
    
    def __str__(self):
        return str(self.content_object) + "  -  " + str(self.user) + "  :  " + str(self.id)
   
    def children(self):
        return Comment.objects.filter(parent=self)
    

#--------------subclasses------------------------

    class Meta:
        ordering = ['-updated','-timestamp']

#---------------property------------------
    @property 
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
    


    


    