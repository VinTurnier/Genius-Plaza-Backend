# Django Application Imports
from django.test import TestCase
from django.contrib.auth import get_user_model

# Local Application Imports
from core.models import Recipe, Ingredient, Step

class ModelTest(TestCase):

    def test_create_user(self):
        ''' test to see if we can create a user'''
        first_name = 'foo'
        last_name = 'bar'
        username ='foobar'
        email = 'foobar@example.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_create_new_recipe(self):
        ''' creates a new recipe from a given user'''
        first_name = 'foo'
        last_name = 'bar'
        username ='foobar'
        email = 'foobar@example.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        name = 'Cookie'
        recipe = Recipe(name=name,user=user)
        recipe.save()

        self.assertEqual(recipe.name,name)
    
    def test_recipe_relationship_with_user(self):
        ''' test the relationship between user and recipe'''
        first_name = 'foo'
        last_name = 'bar'
        username ='foobar'
        email = 'foobar@example.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        name = 'Cookie'
        recipe = Recipe(name=name,user=user)
        recipe.save()
        self.assertEqual(user.recipes.values()[0]['name'],name)
    
    def test_recipe_relationship_with_ingredients(self):
        ''' test the relationship between recipe and ingredients'''
        first_name = 'foo'
        last_name = 'bar'
        username ='foobar'
        email = 'foobar@example.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        name = 'Cookie'
        recipe = Recipe(name=name,user=user)
        recipe.save()
        text='Cookie dough'
        ingredient = Ingredient(text=text, recipe=recipe)
        ingredient.save()
        self.assertEqual(recipe.ingredients.values()[0]['text'],text)

    def test_recipe_relationship_with_steps(self):
        ''' test the relationship between recipe and steps'''
        first_name = 'foo'
        last_name = 'bar'
        username ='foobar'
        email = 'foobar@example.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        name = 'Cookie'
        recipe = Recipe(name=name,user=user)
        recipe.save()
        step_text = 'open the cookie dough'
        step = Step(step_text=step_text,recipe=recipe)
        step.save()
        self.assertEqual(recipe.steps.values()[0]['step_text'],step_text)