from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    mera_post = models.TextField(blank=True, null=True)

    # def save(self)