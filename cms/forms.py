from django import forms

from .models import Unit


class UnitForm(forms.ModelForm):
    text = forms.CharField(max_length=200, required=False)
    answer = forms.CharField(max_length=200, required=False)
    right_comment = forms.CharField(max_length=200, required=False)
    wrong_comment = forms.CharField(max_length=200, required=False)
    url = forms.CharField(max_length=200, required=False)
    right_extra = forms.ModelChoiceField(queryset=Unit.objects.all(), required=False)
    wrong_extra = forms.ModelChoiceField(queryset=Unit.objects.all(), required=False)

    class Meta:
        model = Unit
        fields = ["text", "url", "answer", "right_comment", "wrong_comment", "right_extra", "wrong_extra", "unit_type"]