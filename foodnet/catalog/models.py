<<<<<<< HEAD
from distutils.command.upload import upload
=======

>>>>>>> 39d2d6dc2ef76ac97e11ee0ede483f922f9e4ce7
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Visitor(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
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

    creator = models.ForeignKey(
        'Visitor', on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    preview = models.ImageField(
<<<<<<< HEAD
        null=True, upload_to='uploads/%Y/%m/%d/', default='NULL')
    date = models.DateTimeField(auto_created=True)
=======
        upload_to='images/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)
>>>>>>> 39d2d6dc2ef76ac97e11ee0ede483f922f9e4ce7

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'index'


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
    order = models.PositiveSmallIntegerField(default=1)  # переделать

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
