# Rest Framwork Application Imports
from rest_framework.response import Response
from rest_framework import generics

# Django Application Imports
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Local Application Imports
from core.models import Recipe, Ingredient, Step
from recipe.serializers import IngredientSerializer, StepSerializer, RecipeSerializer

class RecipeViewSet(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, resp):
        user = get_object_or_404(get_user_model(),id = self.request.data.get('user_id'))
        return resp.save(user=user)
    

class SingleRecipeViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
