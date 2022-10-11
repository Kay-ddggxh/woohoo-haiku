from django.contrib import admin
from .models import Haiku, Tanka
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Haiku)
class HaikuAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author')  # add tag list item later
    search_fields = ['title']   # add tag field later
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('create_date',)  # add tag filter later
    summernote_fields = ('content')


@admin.register(Tanka)
class HaikuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'approved')    # add tag later
    search_fields = ['name']    # add tag later
    list_filter = ('approved', 'create_date')   # tag later
    summernote_fields = ('body')

    # possibly add approve method here
