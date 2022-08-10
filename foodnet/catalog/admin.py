from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Visitor)
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(FriendList)
admin.site.register(Grade)
