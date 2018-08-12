from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=10,unique=True)
    news = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.news[:25], "...."
    

