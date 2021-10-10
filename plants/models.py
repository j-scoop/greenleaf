from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-plant.png', upload_to='plant-pics')

    def __str__(self):
        return self.name
