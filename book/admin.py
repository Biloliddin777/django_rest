from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'date_of_birth', 'image')}),
    )


admin.site.register(User, CustomUserAdmin)
