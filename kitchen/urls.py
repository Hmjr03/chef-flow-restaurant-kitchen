from django.urls import path

from kitchen import views

app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    path("dishes/", views.dish_list, name="dish-list"),
    path("dishes/<int:pk>/", views.dish_detail, name="dish-detail"),
    path("cooks/", views.cook_list, name="cook-list"),
    path("ingredients/", views.ingredient_list, name="ingredient-list"),
    path("dish-types/", views.dish_type_list, name="dish-type-list"),
]
