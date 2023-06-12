from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *

class MetricsViewSet(viewsets.ModelViewSet):
	serializer_class = EnergySerializer
	queryset = Energy.objects.all()

	def get_queryset(self, pk=None):
		start = self.request.query_params.get('start')
		end = self.request.query_params.get('end')

		try:
			if start and end:
				return Energy.objects.filter(time_series__range=[start,end])
			else:
				return Energy.objects.all()
		except Energy.DoesNotExist as e:
			return Response(status=status.HTTP_404_NOT_FOUND)


   	