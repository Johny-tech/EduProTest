
# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from .models import *
import json
from .serializers import (
	TestListSerializer,
	# TestCreateSerializer
	QuestionSerializer
)


class TestListView(generics.ListAPIView):
	queryset = Test.objects.all()
	serializer_class = TestListSerializer

class TestCreateView(generics.CreateAPIView):
	queryset  = Test.objects.all()
	serializer_class = TestListSerializer


	def create(self, request, *args, **kwargs):

		serializer = self.get_serializer(data=request.data)
		
		serializer.is_valid(raise_exception=True)
		
		self.perform_create(serializer)
		
		headers = self.get_success_headers(serializer.data)
		
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class QuestionCreateView(generics.CreateAPIView):
	queryset = Test.objects.all()
	serializer_class = QuestionSerializer

	def create(self, request, *args, **kwargs):

		serializer = self.get_serializer(data=request.data)
		
		serializer.is_valid(raise_exception=True)
		
		self.perform_create(serializer)
		
		headers = self.get_success_headers(serializer.data)
		
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
