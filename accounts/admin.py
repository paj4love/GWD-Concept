from django.contrib import admin
from accounts.models import UserProfile
from accounts.models import NewsletterUser


# Register your models here.
admin.site.register(UserProfile)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NewsletterUser, NewsletterAdmin)