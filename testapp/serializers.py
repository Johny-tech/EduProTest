from rest_framework import serializers
from .models import  * 



class OptionSerialiazer(serializers.HyperlinkedModelSerializer):



	class Meta:
		model = Option
		fields = ('option_char','option_text')




class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	
	option = OptionSerialiazer(many=True)
	
	class Meta:
		model = Question
		fields = '__all__'


	def create(self, validated_data):
		options = validated_data.questions.pop('option')
		option_collection = Test.objects.questions.create(**validated_data)
		option_collection.option = []
		for option in options:
			option_collection.option.append(option)
		option_collection.save()
		return option_collection



class TestListSerializer(serializers.HyperlinkedModelSerializer):

	questions = QuestionSerializer(many=True) 

	class Meta:
			model = Test
			fields = '__all__'

		