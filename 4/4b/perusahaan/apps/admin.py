from django.contrib import admin

# Register your models here.

from apps.models import Users_tb, Skill_tb

admin.site.register(Users_tb)
admin.site.register(Skill_tb)
