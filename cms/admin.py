from django.contrib import admin
from django import forms

# Register your models here.
from .models import *

admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Lesson)


class UnitForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)

    class Meta:
        model = Unit
        fields = ["name", "url", "unit_type"]


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm


admin.site.register(Unit, UnitAdmin)
