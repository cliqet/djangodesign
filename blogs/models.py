from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.title} by {self.author.first_name} {self.author.last_name}'

    def username(self):
        return self.author.username

    def blog_author(self):
        return '{} {}'.format(self.author.first_name, self.author.last_name)

    def id(self):
        return self.id