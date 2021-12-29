from django.urls import path
from rest_framework.routers import DefaultRouter
from skuapp.views import CategoryView, DepartmentView, LocationView, ProductSkuView, SubCategoryView, search_product_sku

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
    path(
        'location/<location_id>/department/<department_id>/category/<category_id>/subcategory/',
        SubCategoryView.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='Sub Category List',
    ),
    path(
        'location/<location_id>/department/<department_id>/category/<category_id>/subcategory/<pk>/',
        SubCategoryView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='Sub Category Instance',
    ),
    path(
        'location/<location_id>/department/<department_id>/category/<category_id>/subcategory/<sub_category_id>/product/',
        ProductSkuView.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='Product SKU List',
    ),
    path(
        'location/<location_id>/department/<department_id>/category/<category_id>/subcategory/<sub_category_id>/product/<pk>',
        ProductSkuView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='Product SKU Instance',
    ),
    path(
        'search/',
        search_product_sku,
        name='search product'
    )
] + router.urls
