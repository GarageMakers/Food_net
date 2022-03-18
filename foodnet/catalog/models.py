from ast import Delete
from email.policy import default
from tkinter import CASCADE
from django.db import models


class User(models.Model):

    user_id = models.AutoField()

    name = models.CharField(max_length=30, help_text="Имя Фамилия")
    eMail = models.EmailField()
    isBanned = models.BooleanField(default=False)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author_id = models.AutoField()
    user_id = models.ForeignKey(on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    preview = models.ImageField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    recept_id = models.ForeignKey(on_delete=CASCADE)

    author = models.CharField(max_length=30)
    text_field = models.TextField()

    def __str__(self):
        return self.name


class Step(models.Model):

    step_id = models.AutoField()
    recept_id = models.ForeignKey(on_delete=CASCADE)

    text_field = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.text_field[:6]


class Ingredient(models.Model):

    igr_id = models.AutoField()
    recept_id = models.ForeignKey(on_delete=CASCADE)

    count = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_id = models.AutoField()
    step_id = models.ForeignKey(on_delete=CASCADE)

    path = models.ImageField()

    def __str__(self):
        return self.path
