from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # we add this function to be more accurte when we call te user profile
    def __str__(self):
        return f'{self.user.username} Profile'

    # create a function to override save method to resize imgs that the user upload to not be large and slow down the performance
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


