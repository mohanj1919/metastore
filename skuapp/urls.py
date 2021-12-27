from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from skuapp.views import CategoryView, DepartmentView, LocationView

router = DefaultRouter()
router.register(r'location', LocationView, basename='location')

urlpatterns = [
    path(
        'location/<location_id>/department/',
        DepartmentView.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='Department List',
    ),
    path(
        'location/<location_id>/department/<pk>/',
        DepartmentView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='Department Instance',
    ),
    path(
        'location/<location_id>/department/<department_id>/category/',
        CategoryView.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='Category List',
    ),
    path(
        'location/<location_id>/department/<department_id>/category/<pk>/',
        CategoryView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='Category Instance',
    ),
] + router.urls
