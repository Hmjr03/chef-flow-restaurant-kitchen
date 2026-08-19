from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import (
    Dish,
    DishType,
    Ingredient,
)


User = get_user_model()


class KitchenViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="chef_test",
            password="testpassword123",
            years_of_experience=5,
        )

        self.client.login(
            username="chef_test",
            password="testpassword123",
        )

        self.dish_type = DishType.objects.create(
            name="Main Course",
        )

        self.ingredient = Ingredient.objects.create(
            name="Tomato",
        )

        self.dish = Dish.objects.create(
            name="Pasta",
            description="Fresh pasta with tomato sauce",
            price="15.50",
            dish_type=self.dish_type,
        )

        self.dish.ingredients.add(
            self.ingredient
        )


    def test_dashboard_page_access(self):

        response = self.client.get(
            reverse("kitchen:index")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "ChefFlow",
        )


    def test_dish_list_page_access(self):

        response = self.client.get(
            reverse("kitchen:dish-list")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Pasta",
        )


    def test_create_dish(self):

        response = self.client.post(
            reverse("kitchen:dish-create"),
            {
                "name": "Pizza",
                "description": "Italian pizza",
                "price": "20.00",
                "dish_type": self.dish_type.id,
                "ingredients": [
                    self.ingredient.id,
                ],
            },
        )


        self.assertEqual(
            response.status_code,
            302,
        )


        self.assertTrue(
            Dish.objects.filter(
                name="Pizza"
            ).exists()
        )


    def test_update_dish(self):

        response = self.client.post(
            reverse(
                "kitchen:dish-update",
                args=[self.dish.id],
            ),
            {
                "name": "Updated Pasta",
                "description": "Updated description",
                "price": "18.00",
                "dish_type": self.dish_type.id,
                "ingredients": [
                    self.ingredient.id,
                ],
            },
        )


        self.assertEqual(
            response.status_code,
            302,
        )


        self.dish.refresh_from_db()


        self.assertEqual(
            self.dish.name,
            "Updated Pasta",
        )


    def test_delete_dish(self):

        response = self.client.post(
            reverse(
                "kitchen:dish-delete",
                args=[self.dish.id],
            )
        )


        self.assertEqual(
            response.status_code,
            302,
        )


        self.assertFalse(
            Dish.objects.filter(
                id=self.dish.id
            ).exists()
        )



class AuthenticationTests(TestCase):

    def test_login_required_for_dish_create(self):

        response = self.client.get(
            reverse("kitchen:dish-create")
        )

        self.assertEqual(
            response.status_code,
            302,
        )


    def test_user_can_login(self):

        user = User.objects.create_user(
            username="login_user",
            password="password123",
        )


        response = self.client.post(
            reverse("login"),
            {
                "username": "login_user",
                "password": "password123",
            },
        )


        self.assertEqual(
            response.status_code,
            302,
        )
