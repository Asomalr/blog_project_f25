from django.db import models

# Create your models here.

STATUS =(
    (0, "Draft"),
    (1, "Published"),
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)