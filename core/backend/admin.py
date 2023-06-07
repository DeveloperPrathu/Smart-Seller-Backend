from django.contrib import admin
from django.contrib.admin import register

from backend.models import User, Otp, Token, PasswordResetToken, Category, Slide


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'fullname', 'created_at']
    readonly_fields = ['password']


@register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['phone', 'otp', 'validity', 'verified']


@register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'user', 'created_at']


@register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'user', 'validity']


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image']


@register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['position', 'image']