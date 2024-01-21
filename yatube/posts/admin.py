from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")  # можно добавить pk
    search_fields = ("text",)   # поиск по тексту постов
    list_filter = ("pub_date",)  # фильтрация по дате
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
