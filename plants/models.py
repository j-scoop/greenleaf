from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Plant(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-plant.png', upload_to='plant-pics')

    # TODO:
    # watered = list of dates watered
    # notes = list of text entries
    #

    def __str__(self):
        return self.name

    def save(self):
        super().save()  # run the parent class' save method

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'pk': self.pk})
