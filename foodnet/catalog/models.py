from django.db import models
from django.contrib.auth.models import User


class Visitor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visitor_id = models.AutoField(primary_key=True)
    isBanned = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.username


class Recipe(models.Model):

    recipe_id = models.AutoField(primary_key=True)

    creator_id = models.ForeignKey('Visitor', on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    preview = models.ImageField(default="../images/default.png")
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Comment(models.Model):

    user_id = models.ForeignKey('Visitor', on_delete=models.CASCADE)

    recept_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    text_field = models.TextField()

    def __str__(self):
        return self.text_field[:11]+'...'


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


class FriendList(models.Model):
    friend_one_id = models.ForeignKey(
        'Visitor', on_delete=models.PROTECT, related_name='friend_one_set')
    friend_two_id = models.ForeignKey(
        'Visitor', on_delete=models.PROTECT, related_name='friend_two_set')
    friendship = models.BooleanField(default=False)

    def __str__(self):
        return f"Друзья"
