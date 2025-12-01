from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_desc = models.TextField()
    def __str__(self):
        return self.blog_title

class comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name="comment")
    comment_desc = models.TextField()
    
    def __str__(self):
        return self.comment_desc