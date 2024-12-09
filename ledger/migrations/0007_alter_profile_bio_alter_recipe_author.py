# Generated by Django 5.0.3 on 2024-03-15 06:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(255, 'the field must contain at least 255 characters')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.profile'),
        ),
    ]
