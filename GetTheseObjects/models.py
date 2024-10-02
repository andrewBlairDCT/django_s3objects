from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    type = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
