# Rest Framework Application Imports
from rest_framework import serializers

# Django Application Imports
from django.contrib.auth import get_user_model

# Local Application Imports
from recipe.serializers import RecipeSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','first_name','last_name','username','email','password']
        extra_kwargs = {'password':{'write_only':True,'min_length':7}}

    def create(self, validate_data):
        return get_user_model().objects.create_user(**validate_data)


class SingleUserSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True,read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','email','recipes']