from django import forms
from . models import Post

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

MEDIA_CHOICES = (
    ('magazine', 'Magazine'),
    ('radio', 'Radio Station'),
    ('journal', 'Journal'),
    ('tv', 'TV Station'),
    ('newspaper', 'Newspaper'),
    ('website', 'Website'),
) 
POSITION_CHOICES = (
    ('sr_manager', 'Sr.Manager'),
    ('manager', 'Manager'),
    ('add_manager', 'Add.Manager'),
    ('ast_manager', 'Ast.Manager'),
   
)   
class CustomPost(forms.ModelForm):
    fruit = forms.ChoiceField(choices=FRUIT_CHOICES,widget=forms.RadioSelect())
    media_choice = forms.MultipleChoiceField(choices=MEDIA_CHOICES, widget=forms.CheckboxSelectMultiple())
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=False)
    class Meta:
        model = Post
        fields ='__all__'