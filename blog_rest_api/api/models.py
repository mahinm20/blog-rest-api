from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.author_name

class Blog(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(null=True,blank=True)
    downvote = models.IntegerField(null=True,blank=True)
    writer = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    commentor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} by {} on {} '.format(self.body,self.commentor,self.post)



    
