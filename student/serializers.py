from rest_framework import serializers 
import json
from .models import Test , Question , Option


class QuestionSerializer(serializers.ModelSerializer):

	class Meta:
		model


class TestSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Test
		fields='__all__'
