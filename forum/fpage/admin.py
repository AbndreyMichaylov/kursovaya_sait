from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth.models import User

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Post)
admin.site.register(models.Comment)
