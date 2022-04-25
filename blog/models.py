from django.db import models


# class Users(models.Model):
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
from django.urls import reverse


class Team(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.name


class Breed_cat(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Breed_dog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Sex(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Cat(models.Model):
    text = models.TextField()
    sex = models.ForeignKey(Sex, related_name='post_cat', on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed_cat, related_name='post', on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    img = models.ImageField(upload_to='articles/')

    def get_absolute_url(self):
        return reverse('cat_list', kwargs={'pk': self.id})


class Dog(models.Model):
    text = models.TextField()
    sex = models.ForeignKey(Sex, related_name='post_dog', on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed_dog, related_name='post', on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    img = models.ImageField(upload_to='articles/')

    def get_absolute_url(self):
        return reverse('dog_list', kwargs={'pk': self.id})
