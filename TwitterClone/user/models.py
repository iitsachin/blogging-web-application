from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class profile(models.Model):
    # set one to one relationship with User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pic')

    def __str__(self):
        return f'Profile of {self.user.username}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
