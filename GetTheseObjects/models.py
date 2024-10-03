from django.db import models

class Image(models.Model):
    file_name = models.CharField(max_length=300)
    file_url = models.CharField(max_length=300)
    original_file_name = models.CharField(max_length=300)
    date_last_modified = models.DateTimeField()
    file_type = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
