from django.contrib.postgres import serializers

from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        #serializers = converts python to json
        #json to python = deserializers



