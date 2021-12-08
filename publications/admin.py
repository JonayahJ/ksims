# Publications admin
from django.contrib import admin
from .models import Article

# Article
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'post_date')
    search_fields = ('title',)
    ordering = ('post_date',)


admin.site.register(Article, ArticleAdmin)
