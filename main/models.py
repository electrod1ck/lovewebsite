from django.db import models


class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.image.name


