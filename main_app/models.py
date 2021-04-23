from django.db import models
from django.urls import reverse

# Create your models here.
class Wishlist(models.Model):
    description = models.TextField(max_length=4096)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('index')

