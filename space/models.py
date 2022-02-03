from django.db import models


# Create your models here.
class spaceship(models.Model):

    name = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    image = models.ImageField(upload_to="pics",
                              height_field=None,
                              width_field=None,
                              max_length=None)
