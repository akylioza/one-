from django.contrib import admin
from . import models

admin.site.register(models.Book)
admin.site.register(models.Rating)
admin.site.register(models.BookComment)
admin.site.register(models.Expert)
admin.site.register(models.ExpertRecomendation)