from django.db import models

# Create your models here.
class Note(models.Model):
    author = models.CharField(max_length=200)
    course = models.TextField()
    body = models.TextField()
    genre = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author + ': ' + self.body
