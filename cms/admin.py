from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Lesson)
admin.site.register(Unit)
