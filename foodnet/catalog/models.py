from django.db import models
import uuid
from django.core.validators import EmailValidator


class User(models.Model):

    user_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30, help_text="Имя Фамилия")
    eMail = models.EmailField(validators=[EmailValidator])
    isBanned = models.BooleanField(default=False)
    password = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    recipe_id = models.AutoField(primary_key=True)

    creator_id = models.ForeignKey('User', on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    preview = models.ImageField(default="../images/default.png")
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):

    comment_id = models.AutoField(primary_key=True)

    recept_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)

    text_field = models.TextField()

    def __str__(self):
        return self.name


class Step(models.Model):

    recept_id = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, null=True)

    text_field = models.TextField()
    photo_path = models.ImageField(null=True, default='NULL')
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.text_field[:11]+'...'


class Ingredient(models.Model):

    recept_id = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, null=True)

    count = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserList(models.Model):

    owner_id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self):
        pass

    class Meta:
        abstract = True


class FriendList(UserList):
    def __str__(self):
        return f"Друзья"


class BlackList(UserList):
    def __str__(self):
        return f"Черный список"
