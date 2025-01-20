from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.username}"
# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content}"