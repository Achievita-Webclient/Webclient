from django.db import models
from django.contrib.auth.models import User

#This is basically for switching item uploads 
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

#Using some codes from our faq codes on fb to save time
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    #not complicated shaa
    def __str__(self):
        return self.title
        
