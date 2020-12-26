from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# for restrict post to display which at draft means cheak whether cheak status of post published or not before post
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')



# Create your models here.
from taggit.managers import TaggableManager
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
# slug:- to provide SEO i.e. user fraindly url*********
    author = models.ForeignKey(User,related_name='blog_posts' ,on_delete=models.CASCADE)
# compulsory this authoe should be valid user from user database
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
# this considered defalt time zone>>>>>>>>>>>>>>>>>
    created=models.DateTimeField(auto_now_add=True)
# post object created or added in database time automatically date and time will be considered
    updated=models.DateTimeField(auto_now=True)
# last time whenever you call save() method this time will be considered>>>>>
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
# this is defalt taggit manager to apply tag to each post
    tags=TaggableManager()


    class Meta:
        ordering=('-publish',)
            #****decending date of published most recent date will be indicate

    def __str__(self):
        return self.title
        # *****if any where published you post just display  title****
    

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

# *************************************************************************************

# model related to comment section**********
# comments have one to many relation ship that by using foreign key

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    # related_name='comments' This is uswd for related that post take all comments..
    name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    body=models.TextField(max_length=256)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    # ordering is important for comments........last cooment is first or first comment as per your requirement
    class Meta:
        ordering=('-created',)
        # ordering recent to old
    def __str__(self):
        return 'commented by {} on {}' .format(self.name,self.post)



