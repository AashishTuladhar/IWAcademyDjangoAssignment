import sys
from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=128)

    def __str__(self):
        return self.author_name

class Blogs(models.Model):
    blog_title = models.CharField(max_length=128)
    blog_content = models.TextField(max_length=sys.maxsize)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
