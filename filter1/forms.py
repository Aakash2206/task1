from django import forms
from django.forms import ModelForm

"""from filter1.models import Data

CAT_CHOICES = [
    ('Category 1', 'category 1'),
    ('Category 2', 'category 2'),
]


class Sort(forms.ModelForm):
    category = forms.CharField(label='Sort', widget=forms.Select(choices=CAT_CHOICES))

    class Meta:
        model = Data
        fields = ['cat']
"""
from filter1.models import Data


class Sort(forms.Form):
    cat = forms.ChoiceField(choices=[(x, x) for x in range(0, 2)])

    class Meta:
        fields = ('cat',)


'''
from django import forms
from .models import Data


class Sort(forms.Form):
    cat = forms.CharField(label='CATEGORY', widget=forms.Select(choices=CAT_CHOICES))

    class Meta:
        model = Data
        fields = ['cat']
'''
