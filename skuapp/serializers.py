import logging
from django.core.exceptions import ValidationError
from rest_framework import serializers

from skuapp.models import (
    Location,
    Department,
    Category,
    ProductSku,
)
logger = logging.getLogger(__name__)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'location']

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'super_category', 'department']

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "super_category": instance.super_category.name if instance.super_category else ""
        }


class ProductSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "location": instance.location.name if instance.location else "",
            "category": instance.department.name if instance.department else "",
            "category": instance.category.name if instance.category else "",
            "sub_category": instance.sub_category.name if instance.sub_category else "",
        }
