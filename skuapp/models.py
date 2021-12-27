from django.db import models
from django.db.models.deletion import CASCADE


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=255, db_index=True)
    location = models.ManyToManyField(to=Location, related_name="location_departments")

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=255, db_index=True)
    super_category = models.ForeignKey(to='self', null=True, on_delete=CASCADE)
    department = models.ManyToManyField(to=Department, related_name="department_categories")

    def __str__(self) -> str:
        return self.name


class LocationDepartmentCategorySubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(to=Location, on_delete=CASCADE)
    department = models.ForeignKey(to=Department, on_delete=CASCADE)
    category = models.ForeignKey(to=Category, on_delete=CASCADE, related_name="category_meta_info")
    sub_category = models.ForeignKey(to=Category, on_delete=CASCADE, related_name="sub_category_meta_info")

    def __str__(self) -> str:
        return f'{self.location}, {self.department}, {self.category}, {self.sub_category}'


class ProductSku(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=255, db_index=True)
    meta_info = models.ForeignKey(
        to=LocationDepartmentCategorySubCategory, related_name="products",
        on_delete=CASCADE
    )

    def __str__(self) -> str:
        return self.name
