from django.contrib import admin
from django import forms

# Register your models here.
from .models import *
from .forms import *

admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Lesson)


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm


admin.site.register(Unit, UnitAdmin)
