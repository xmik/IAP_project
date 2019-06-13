from .models import Branch_Offices
from rest_framework import serializers


class Branch_OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch_Offices
        fields = '__all__'