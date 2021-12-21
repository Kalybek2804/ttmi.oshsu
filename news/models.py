from django.db import models
from django_resized import ResizedImageField



class New(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = ResizedImageField(upload_to = 'images', size = [1280, 720])
    create_date = models.DateField(auto_now_add=True)
    news_view = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.title} - {self.create_date}'


    