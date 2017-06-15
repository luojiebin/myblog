from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Post, About


admin.site.site_header = 'Blog Administration'


def publish_post(modeladmin, request, queryset):
    queryset.update(publish=True)
publish_post.short_description = 'Publish Post'


def draft_post(modeladmin, request, queryset):
    queryset.update(publish=False)
draft_post.short_description = 'Draft Post'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'modified')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    prepopulated_fields = {'slug': ('title',)}
    actions = (publish_post, draft_post,)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    def has_add_permission(self, request):
        if not About.objects.count():
            return True
        return False
