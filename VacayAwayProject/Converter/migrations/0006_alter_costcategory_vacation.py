# Generated by Django 4.2.1 on 2023-06-10 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Converter', '0005_remove_costcategory_latestconversionrate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costcategory',
            name='vacation',
            field=models.ForeignKey(blank=True, db_column='vacationId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Converter.vacation'),
        ),
    ]
