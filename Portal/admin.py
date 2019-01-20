from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Voter, Post, Nominee

# Register your models here.

@admin.register(Voter)
class VoterAdmin(ImportExportModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'name', 'class_sec', 'house', 'stage')
    list_display_links = ('username', 'name')
    list_filter = ('class_sec',)
    ordering = ('id',)
    search_fields = ('username', 'name')
    list_per_page = 35

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'type')
    list_display_links = ('id', 'name', 'type')
    ordering = ('id',)

@admin.register(Nominee)
class NomineeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'post', 'house', 'votes')
    list_display_links = ('id', 'name', 'post', 'house', 'votes')
    list_filter = ('post__type', 'post', 'house',)
    ordering = ('id','votes')
