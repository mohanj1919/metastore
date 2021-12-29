
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from skuapp.serializers import CategorySerializer, DepartmentSerializer, LocationSerializer, ProductSkuSerializer
from skuapp.models import Category, Department, Location, ProductSku


@api_view(http_method_names=['GET', 'POST'])
def locations_list(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response("test")


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DepartmentView(ModelViewSet):
    serializer_class = DepartmentSerializer
    location = None

    def get_serializer(self, *args, **kwargs):
        self.get_queryset()
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            data = kwargs['data']
            data['location'] = [self.location.id]
            kwargs['data'] = data
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        location_id = self.request.parser_context['kwargs'].get('location_id')
        location = get_object_or_404(Location.objects.all(), id=location_id)
        self.location = location
        return Department.objects.filter(location=location)


class CategoryView(DepartmentView):
    serializer_class = CategorySerializer
    department = None

    def get_serializer(self, *args, **kwargs):
        self.get_queryset()
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            data = kwargs['data']
            data['department'] = [self.department.id]
            kwargs['data'] = data
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        department_id = self.request.parser_context['kwargs'].get('department_id')
        location_departments = super().get_queryset()
        department = get_object_or_404(
            location_departments, id=department_id
        )
        self.department = department
        return Category.objects.filter(department=department)


class SubCategoryView(CategoryView):
    super_category = None

    def get_serializer(self, *args, **kwargs):
        self.get_queryset()
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            data = kwargs['data']
            data['department'] = [self.department.id]
            data['super_category'] = self.super_category.id
            kwargs['data'] = data
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        category_id = self.request.parser_context['kwargs'].get('category_id')
        department_categories = super().get_queryset()
        super_category = get_object_or_404(
            department_categories, id=category_id
        )
        self.super_category = super_category
        return Category.objects.filter(super_category=super_category)


class ProductSkuView(SubCategoryView):
    serializer_class = ProductSkuSerializer
    sub_category = None

    def get_serializer(self, *args, **kwargs):
        self.get_queryset()
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            data = kwargs['data']
            data['category'] = self.super_category.id
            data['sub_category'] = self.sub_category.id
            data['location'] = self.location.id
            data['department'] = self.department.id
            kwargs['data'] = data
        return ProductSkuSerializer(*args, **kwargs)

    def get_queryset(self):
        sub_category_id = self.request.parser_context['kwargs'].get('sub_category_id')
        categories = super().get_queryset()
        sub_category = get_object_or_404(
            categories, id=sub_category_id
        )
        self.sub_category = sub_category
        return ProductSku.objects.filter(sub_category=sub_category)


@api_view(http_method_names=['POST'])
def search_product_sku(request, *args, **kwargs):
    breakpoint()
    data = request.data
    try:
        location, department, category, sub_category = data.split(', ')
        products = ProductSku.objects.filter(
            location_id__in=Location.objects.filter(name=location).values_list('id'),
            department_id__in=Department.objects.filter(name=department).values_list('id'),
            category_id__in=Category.objects.filter(name=category).values_list('id'),
            sub_category_id__in=Category.objects.filter(name=sub_category).values_list('id')
        ).values_list('id', flat=True)
        return HttpResponse(products)
    except ValueError as e:
        raise ValidationError(
            "please provide valid search query in 'location, department, category, sub_category' order"
        )
