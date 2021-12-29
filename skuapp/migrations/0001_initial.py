# Generated by Django 4.0 on 2021-12-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSku',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category_meta_info', to='skuapp.category')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='skuapp.department')),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='skuapp.location')),
                ('sub_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category_meta_info', to='skuapp.category')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.ManyToManyField(related_name='location_departments', to='skuapp.Location'),
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ManyToManyField(related_name='department_categories', to='skuapp.Department'),
        ),
        migrations.AddField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skuapp.category'),
        ),
    ]
