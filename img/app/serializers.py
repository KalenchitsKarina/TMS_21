from rest_framework import serializers
from .models import NatureImage


class NatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatureImage
        fields = ('width', 'height')