# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Member, FinanceOfficer

# # Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email','is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         # ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Member)
# admin.site.register(FinanceOfficer)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Member, FinanceOfficer

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


# Define admin classes for Member and FinanceOfficer
@admin.register(Member)
class MemberAdmin(UserAdmin):
    list_display = ('email', 'staff_id', 'full_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'staff_id', 'full_name', 'gender', 'birthdate', 'date_employed', 'contributed_months', 'basic_salary', 'accumulated_contributions')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'staff_id', 'full_name', 'gender','birthdate','date_employed','contributed_months','basic_salary','accumulated_contributions','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'staff_id', 'full_name')
    ordering = ('email',)

@admin.register(FinanceOfficer)
class FinanceOfficerAdmin(UserAdmin):
    list_display = ('email', 'staff_id', 'gender', 'birthdate', 'date_employed', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'staff_id', 'gender', 'birthdate', 'date_employed')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'staff_id','gender', 'birthdate', 'date_employed', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'staff_id')
    ordering = ('email',)