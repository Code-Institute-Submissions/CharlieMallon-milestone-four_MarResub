from django.contrib import admin
from .models import Faqs

# Register your models here.
class faqsAdmin(admin.ModelAdmin):
    list_display = (
        "faq_title",
        "faq_content",
    )

    ordering = ('faq_title',)

admin.site.register(Faqs, faqsAdmin)