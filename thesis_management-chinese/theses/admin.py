# theses/admin.py
from django.contrib import admin
from .models import Thesis

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'student__username')
