# Generated by Django 4.0.1 on 2022-01-19 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_productvariants_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariants',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.product'),
        ),
    ]
