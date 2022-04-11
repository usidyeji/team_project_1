from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Tag
# Register your models here.

admin.site.register(Post, MarkdownxModelAdmin)

class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag, TagAdmin)