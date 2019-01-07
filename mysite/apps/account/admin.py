from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.account.models import Account, Work, Group, AddToGroup, WorkResponse

class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'account'

class UserAdmin(BaseUserAdmin):
    inlines = (AccountInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Work)
admin.site.register(Group)
admin.site.register(AddToGroup)
admin.site.register(WorkResponse)
