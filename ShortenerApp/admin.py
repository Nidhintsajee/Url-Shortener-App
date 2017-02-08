from django.contrib import admin
from ShortenerApp.models import Urls
# Register your models here.

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'date_submitted', 'usage_count')
    ordering = ('-date_submitted',)


admin.site.register(Urls, UrlsAdmin)  # Register the Urls model with UrlsAdmin options
