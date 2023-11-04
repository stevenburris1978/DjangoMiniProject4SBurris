from django.contrib import admin

from .models import Choice, Socialpost


admin.site.site_header = "Social App Administration"

# Customize the display columns in the admin list


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["post_title", "description", "image"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["post_title", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["post_title"]


admin.site.register(Choice)
admin.site.register(Socialpost, PostAdmin)
