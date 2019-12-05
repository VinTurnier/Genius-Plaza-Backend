# Django Application Imports
from django.urls import path

# Local Application Imports
from recipe.views import RecipeViewSet, SingleRecipeViewSet

app_name = 'recipe'

urlpatterns = [
    path('recipes/',RecipeViewSet.as_view(),name='recipes'),
    path('recipes/<int:pk>',SingleRecipeViewSet.as_view(),name='recipe')
]
