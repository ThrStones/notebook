from django.contrib import admin

# Register your models here.
from readnovel.models import NovelInfo, Chapter

admin.site.register(NovelInfo)
admin.site.register(Chapter)
