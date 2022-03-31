from email.policy import default
from django.db import models
import uuid


class User(models.Model):

    user_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30, help_text="Имя Фамилия")
    eMail = models.EmailField()
    isBanned = models.BooleanField(default=False)
    password = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    author_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    preview = models.ImageField(default="../images/default.png")
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):

    recept_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    author = models.CharField(max_length=30)
    text_field = models.TextField()

    def __str__(self):
        return self.name


class Step(models.Model):

    recept_id = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, null=True)

    text_field = models.TextField()
    photo_path = models.ImageField()

    def __str__(self):
        return self.text_field[:6]


class Ingredient(models.Model):

    recept_id = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, null=True)

    count = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name


# class Photo(models.Model):
#     photo_id = models.UUIDField(primary_key=True)
#     step_id = models.ForeignKey('Step', on_delete=models.CASCADE)

#     path = models.ImageField()

#     def __str__(self):
#         return self.path
