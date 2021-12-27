import logging
from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers

from skuapp.models import (
    Location,
    Department,
    Category,
    ProductSku,
    LocationDepartmentCategorySubCategory,
)
logger = logging.getLogger(__name__)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    location = serializers.ListField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'location']

    def validate(self, attrs):
        locations = attrs['location']
        location_ids = []
        try:
            for location_name in locations:
                search_crieteria = {}
                try:
                    search_crieteria['id'] = int(location_name)
                except ValueError as e:
                    search_crieteria['name'] = location_name
                location = Location.objects.get(**search_crieteria)
                location_ids.append(location.id)
            attrs['location'] = location_ids
            return super().validate(attrs)
        except Location.DoesNotExist as e:
            raise ValidationError(str(e))

    def to_representation(self, instance):
        return {
            "name": instance.name,
            "location": instance.location.values_list('name', flat=True)
        }


class CategorySerializer(serializers.ModelSerializer):
    department = serializers.ListField()
    super_category = serializers.CharField(
        required=False,
        allow_null=True
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'super_category', 'department']

    def validate_super_category(self, value):
        search_crieteria = {}
        try:
            search_crieteria['id'] = int(value)
        except ValueError as e:
            search_crieteria['name'] = value
        try:
            category = Category.objects.get(**search_crieteria)
            return category
        except Category.DoesNotExist as e:
            raise ValidationError(str(e))

    def validate(self, attrs):
        departments = attrs['department']
        department_ids = []
        try:
            for department_key in departments:
                search_crieteria = {}
                try:
                    search_crieteria['id'] = int(department_key)
                except ValueError as e:
                    search_crieteria['name'] = department_key
                department = Department.objects.get(**search_crieteria)
                department_ids.append(department.id)
            attrs['department'] = department_ids
            return super().validate(attrs)
        except Department.DoesNotExist as e:
            raise ValidationError(str(e))

    def to_representation(self, instance):
        return {
            "name": instance.name,
            "department": instance.department.values_list('name', flat=True),
            "super_category": instance.super_category.name if instance.super_category else ""
        }


class LocationDepartmentCategorySubCategorySerializer(serializers.Serializer):
    location_name = serializers.CharField(max_length=255, allow_blank=True)
    department_name = serializers.CharField(max_length=255, allow_blank=True)
    category_name = serializers.CharField(max_length=255, allow_blank=True)
    sub_category_name = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = LocationDepartmentCategorySubCategory
        fields = '__all__'

    @staticmethod
    def validate_and_save_data(serializer_class, data):
        try:
            serializer = serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            return serializer.save()
        except ValidationError as e:
            message = f"Error while saving {data} using {serializer_class} serializer. {str(e)}"
            logger.error(
                f"Error while saving {data} using {serializer_class} serializer. {str(e)}", 
                exc_info=True
            )
            raise ValidationError(message=message)

    def save(self, **kwargs):
        validated_data = self.validated_data
        try:
            location = self.validate_and_save_data(LocationSerializer, {"name": validated_data.get('location_name')})
            department = self.validate_and_save_data(LocationSerializer, {"name": validated_data.get('department_name')})
            category = self.validate_and_save_data(LocationSerializer, {"name": validated_data.get('category_name')})
            sub_category = self.validate_and_save_data(LocationSerializer, {"name": validated_data.get('sub_category_name')})
            meta_info = LocationDepartmentCategorySubCategory()
            meta_info.location = location
            meta_info.department = department
            meta_info.category = category
            meta_info.sub_category = sub_category
            meta_info.save()
            return meta_info
        except ValidationError as e:
            raise e


class ProductSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = '__all__'

