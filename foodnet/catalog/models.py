from email.policy import default
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
    user_id = models.ForeignKey()

    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    preview = models.ImageField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    recept_id = models.ForeignKey()

    author = models.CharField(max_length=30)
    text_field = models.TextField()


class Step(models.Model):

    step_id = models.AutoField()
    recept_id = models.ForeignKey()

    text_field = models.TextField()
    photo = models.ImageField()


class Ingredient(models.Model):

    igr_id = models.AutoField()
    recept_id = models.ForeignKey()

    count = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Photo(models.Model):
    photo_id = models.AutoField()
    step_id = models.ForeignKey()

    path = models.ImageField()
