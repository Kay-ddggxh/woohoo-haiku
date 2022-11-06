from .models import Tanka
from django import forms


class TankaForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    submit tankas on haikus
    """
    class Meta:
        model = Tanka
        fields = ('body',)
