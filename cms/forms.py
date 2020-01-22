from django import forms

from .models import Unit


class UnitForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)

    class Meta:
        model = Unit
        fields = ["name", "url", "unit_type"]