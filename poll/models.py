from django.db import models
from django.utils import timezone

class Poll(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ]
    
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    active_until = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpublished')
    
    def is_active(self):
        return self.active_until > timezone.now()
    
    def __str__(self):
        return self.title

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.poll.title} - {self.title}"

class Response(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='responses')
    name = models.CharField(max_length=100)
    response_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.option.title}"