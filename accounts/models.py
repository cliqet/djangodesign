from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime

GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
)

MAX_IMAGE_WIDTH = 300
MAX_IMAGE_HEIGHT = 300

# extend the User model
class AuthorProfile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='user_profile_pics')
    date_of_birth = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    contact_number = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.author.username} Profile'

    def username(self):
        return self.author.username

    def first_name(self):
        return self.author.first_name

    def last_name(self):
        return self.author.last_name

    def id(self):
        return self.id

    # keep profile image to a certain size
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # resize image after saving to save space
        img = Image.open(self.image.path)

        if img.height > MAX_IMAGE_HEIGHT or img.width > MAX_IMAGE_WIDTH:
            output_size = (MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT)
            img.thumbnail(output_size)
            img.save(self.image.path)


