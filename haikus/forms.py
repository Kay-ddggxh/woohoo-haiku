from .models import Tanka
from django import forms


class TankaForm(forms.ModelForm):

    class Meta:
        model = Tanka
        fields = ('body',)
