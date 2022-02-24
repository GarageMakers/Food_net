from django.db import models


# class User(models.Model):
#     name = models.CharField(max_length=30, help_text="Имя Фамилия")
#     eMail = models.EmailField()
#     user_id = models.ForeignKey()

#     def __str__(self):
#         return self.name


# class Recipe(models.Model):
#     name = models.CharField(max_length=20)
#     author = models.CharField(max_length=30)
#     preview = models.ImageField()
#     date = models.DateTimeField()

#     def __str__(self):
#         return self.name


# class CommentList(models.Model):
#     recipe_name = models.CharField(max_length=20)


# class Comment(models.Model):
#     author = models.CharField(max_length=30)
#     text_field = models.TextField()


# class Step(models.Model):
#     text_field = models.TextField()
#     photo = models.ImageField()


# class Ingredient(models.Model):
#     count = models.CharField(max_length=20)
#     type = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name
