from .models import Haiku, Tanka
from django import forms


class HaikuForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    add and save haiku posts
    """
    class Meta:
        model = Haiku
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super(HaikuForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(
            attrs={'placeholder': 'Enter a title'})
        self.fields['content'].widget = forms.Textarea(
            attrs={'placeholder': 'Write haiku here'})


class TankaForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    submit tankas on haikus
    """
    class Meta:
        model = Tanka
        fields = ('body',)
