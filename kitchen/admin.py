from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, Dish, DishType, Ingredient


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("ChefFlow information", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("ChefFlow information", {"fields": ("years_of_experience",)}),
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    list_filter = ("dish_type",)
    search_fields = ("name", "description")
    filter_horizontal = ("cooks", "ingredients")
