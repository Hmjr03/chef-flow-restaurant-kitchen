from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from kitchen.models import Cook, Dish, DishType, Ingredient


def index(request):
    """Display the ChefFlow dashboard."""

    context = {
        "dish_count": Dish.objects.count(),
        "dish_type_count": DishType.objects.count(),
        "cook_count": Cook.objects.count(),
        "ingredient_count": Ingredient.objects.count(),
    }

    return render(request, "kitchen/index.html", context)


@login_required
def dish_list(request):
    """Display all dishes with optional search."""

    query = request.GET.get("q", "").strip()

    dishes = Dish.objects.select_related("dish_type").prefetch_related(
        "ingredients",
        "cooks",
    )

    if query:
        dishes = dishes.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(dish_type__name__icontains=query)
            | Q(ingredients__name__icontains=query)
        ).distinct()

    context = {
        "dishes": dishes,
        "query": query,
    }

    return render(request, "kitchen/dish_list.html", context)


@login_required
def dish_detail(request, pk):
    """Display detailed information about a dish."""

    dish = get_object_or_404(
        Dish.objects.select_related("dish_type").prefetch_related(
            "ingredients",
            "cooks",
        ),
        pk=pk,
    )

    context = {
        "dish": dish,
    }

    return render(request, "kitchen/dish_detail.html", context)


@login_required
def cook_list(request):
    """Display all cooks with optional search."""

    query = request.GET.get("q", "").strip()

    cooks = Cook.objects.all()

    if query:
        cooks = cooks.filter(
            Q(username__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )

    context = {
        "cooks": cooks,
        "query": query,
    }

    return render(request, "kitchen/cook_list.html", context)


@login_required
def ingredient_list(request):
    """Display all ingredients with optional search."""

    query = request.GET.get("q", "").strip()

    ingredients = Ingredient.objects.all()

    if query:
        ingredients = ingredients.filter(name__icontains=query)

    context = {
        "ingredients": ingredients,
        "query": query,
    }

    return render(request, "kitchen/ingredient_list.html", context)


@login_required
def dish_type_list(request):
    """Display all dish types with optional search."""

    query = request.GET.get("q", "").strip()

    dish_types = DishType.objects.all()

    if query:
        dish_types = dish_types.filter(name__icontains=query)

    context = {
        "dish_types": dish_types,
        "query": query,
    }

    return render(request, "kitchen/dishtype_list.html", context)
