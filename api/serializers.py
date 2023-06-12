from rest_framework import serializers
from .models import *

class EnergySerializer(serializers.ModelSerializer):
	class Meta:
		model = Energy
		fields = '__all__'