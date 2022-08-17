from django.contrib import admin

# Register your models here.

from . import models


class TodoAdmin(admin.ModelAdmin):
    """
    Task Admin
    """
    model = models.Todo
    list_display = ["id", "task", "status", "completed", "updated"]
    search_fields = ["id", "task", "status", "completed", "updated"]
    readonly_fields = ('id',)



admin.site.register(models.Todo, TodoAdmin)
