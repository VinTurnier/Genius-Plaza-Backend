# Rest Framework imports
from rest_framework import serializers

# Local Application Imports
from core.models import Recipe, Ingredient, Step

class IngredientSerializer(serializers.ModelSerializer):
    ''' Serializes Ingredients ORM model'''
    class Meta:
        model = Ingredient
        fields = ['text']


class StepSerializer(serializers.ModelSerializer):
    ''' Serializes Step ORM model'''
    class Meta:
        model = Step
        fields = ['step_text']


class RecipeSerializer(serializers.ModelSerializer):
    ''' Serializes Recipe ORM model'''
    ingredients = IngredientSerializer(many=True)
    steps = StepSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ['id','name','ingredients','steps']


    def create(self, validated_data):
        ''' Creates a new recipe with ingredients an steps
        :param validated_data: data sent from api endpoint
        :return: recipe object
        '''
        ingredients = validated_data.pop('ingredients',None)
        steps = validated_data.pop('steps', None)
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            Ingredient.objects.create(recipe=recipe, text=ingredient['text'])
        for step in steps:
            Step.objects.create(recipe=recipe,step_text=step['step_text'])
        
        return recipe

        
    def update(self, instance, validated_data):
        ''' updates and deletes the recipe, step and ingredients

        :param instance: represnets the orm model in this case recipe
        :param validated data: data sent from api endpoint
        :return: recipe object
        '''
        ingredients_data = validated_data.pop('ingredients',None)
        steps_data = validated_data.pop('steps', None)
        ingredients = (instance.ingredients).all()
        ingredients = list(ingredients)
        steps = (instance.steps).all()
        steps = list(steps)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        for ingredient_data in ingredients_data:
            if ingredients:
                ingredient = ingredients.pop(0)
                ingredient.text = ingredient_data.get('text',ingredient.text)
                ingredient.save()
            else:
                ingredient = Ingredient(text=ingredient_data.get('text'),recipe=instance)
                ingredient.save()
        
        for step_data in steps_data:
            if steps:
                step = steps.pop(0)
                step.step_text = step_data.get('step_text',step.step_text)
                step.save()
            else:
                step = Step(step_text=step_data.get('step_text'),recipe=instance)
                step.save()
        
        return instance