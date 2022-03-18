from django.db import models


class User(models.Model):

    user_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30, help_text="Имя Фамилия")
    eMail = models.EmailField()
    isBanned = models.BooleanField(default=False)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author_id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    preview = models.ImageField()
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

    step_id = models.UUIDField(primary_key=True)
    recept_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    text_field = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.text_field[:6]


class Ingredient(models.Model):

    igr_id = models.UUIDField(primary_key=True)
    recept_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    count = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_id = models.UUIDField(primary_key=True)
    step_id = models.ForeignKey('Step', on_delete=models.CASCADE)

    path = models.ImageField()

    def __str__(self):
        return self.path
