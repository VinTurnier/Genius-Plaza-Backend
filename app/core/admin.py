# Django Application Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Local Application Imports
from core.models import User, Recipe, Ingredient, Step

class UserAdmin(BaseUserAdmin):
    ''' User Admin field management'''
    order_by = ['id']
    list_display = ('first_name','last_name','username','email')
    fieldsets = (
        (None, {'fields': ('username',)}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','username','email','password1', 'password2'),
        }),
    )

''' register admin site models'''
admin.site.register(User,UserAdmin)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Step)
