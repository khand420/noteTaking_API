from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Todo._meta.fields]


admin.site.register(Todo, TodoAdmin)

# Register your models here.
