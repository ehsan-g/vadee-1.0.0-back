from django.contrib import admin
from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import (
    Category,
    Image,
    MyUser,
    Order,
    OrderItem,
    Artwork,
    ShippingAddress,
    SubCategory,
)


class UserAdminConfig(UserAdmin):
    model = MyUser
    search_fields = ('email', 'user_name', 'first_name',
                     'last_name', 'profile_picture')
    list_filter = ('email', 'user_name', 'first_name', 'last_name',
                   'profile_picture', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'profile_picture',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name',
         'first_name', 'last_name', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        MyUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'profile_picture', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )



class CategoryAdminConfig(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class OrderAdminConfig(admin.ModelAdmin):
    model = Order
    list_display = ['created_at']


class OrderItemAdminConfig(admin.ModelAdmin):
    model = OrderItem
    list_display = ['created_at']


# Register your models here.
admin.site.register(MyUser, UserAdminConfig)
admin.site.register(Artwork)
admin.site.register(Artist)
admin.site.register(Favorite)
admin.site.register(Order, OrderAdminConfig)
admin.site.register(OrderItem, OrderItemAdminConfig)
admin.site.register(Category, CategoryAdminConfig)
admin.site.register(SubCategory)
admin.site.register(Image)
admin.site.register(ShippingAddress)