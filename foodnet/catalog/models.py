from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Visitor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visitor_id = models.AutoField(primary_key=True)
    isBanned = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Visitor.objects.create(user=instance, isBanned=False)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.visitor.save()

    def __str__(self):
        return self.user.get_full_name()


class Recipe(models.Model):

    recipe_id = models.AutoField(primary_key=True)

    creator_id = models.ForeignKey('Visitor', on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    preview = models.ImageField(
        null=True, upload_to='uploads/%Y/%m/%d/', default='NULL')
    date = models.DateTimeField(auto_created=True)

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

    text_field = models.TextField(max_length=300)
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
