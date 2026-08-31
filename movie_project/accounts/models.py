from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    profile_photo=models.ImageField(
        upload_to='profiles/',
        blank=True,null=True
    )

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    added_by=models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title=models.CharField(max_length=100)
    poster=models.ImageField(upload_to="poster/")
    description=models.TextField()
    release_date=models.DateField()
    actors=models.TextField()
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    category=models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    trailer_link=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


