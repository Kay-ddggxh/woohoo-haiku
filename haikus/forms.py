from .models import Haiku, Tanka, Tag
from django import forms

choises = Tag.objects.all().values_list('tagname', 'tagname')

CHOICE_LIST = []

CHOICE_LIST.append(("placeholder", "Tag your haiku appropriately"))

for choice in choises:
    CHOICE_LIST.append(choice)


class HaikuForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    add and save haiku posts
    """
    class Meta:
        model = Haiku
        fields = ('title', 'tag', 'content',)

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'tag': forms.Select(choices=CHOICE_LIST),
            'content': forms.Textarea(
                attrs={'placeholder': 'Write Haiku here'})
        }


class TankaForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    submit tankas on haikus
    """
    class Meta:
        model = Tanka
        fields = ('body',)
