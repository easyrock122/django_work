from django.db import models

# Create your models here.
class Designer(models.Model):

    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.name