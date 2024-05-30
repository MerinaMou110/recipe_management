from django.contrib import admin
from .models import Recipe, Ingredient, Rating, Comment

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Rating)
admin.site.register(Comment)
