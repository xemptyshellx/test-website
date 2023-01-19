from django.contrib import admin

# Register your models here.
from portfolio.models import Project


# class ProjectAdmin(admin.ModelAdmin):
#     pass



admin.site.register(Project)
