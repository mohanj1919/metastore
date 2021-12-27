
from django.db import models
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.utils.representation import serializer_repr
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from skuapp.serializers import CategorySerializer, DepartmentSerializer, LocationSerializer
from skuapp.models import Category, Department, Location


@api_view(http_method_names=['GET', 'POST'])
def locations_list(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response("test")


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        location_id = self.request.parser_context['kwargs'].get('location_id')
        location = get_object_or_404(Location.objects.all(), id=location_id)
        return Department.objects.filter(location=location)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        location_id = self.request.parser_context['kwargs'].get('location_id')
        department_id = self.request.parser_context['kwargs'].get('department_id')
        location = get_object_or_404(Location.objects.all(), id=location_id)
        department = get_object_or_404(
            Department.objects.filter(location=location), id=department_id
        )
        return Category.objects.filter(department=department)
