from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return 'Article: ' + self.title
