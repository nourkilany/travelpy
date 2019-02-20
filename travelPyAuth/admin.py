from django.contrib import admin
from django.contrib.auth.models import User
# register the models


class CustomUser(admin.ModelAdmin):
    fieldsets = (["User Area", {'fields':['is_active']}],)
    list_display = ('user_name','is_active')


admin.site.register(User,CustomUser)