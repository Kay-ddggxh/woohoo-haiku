from django.contrib import admin
from .models import Haiku, Tanka
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Haiku, Tanka)
class HaikuAdmin(SummernoteModelAdmin):

    summernote_fields = ('content', 'body')
