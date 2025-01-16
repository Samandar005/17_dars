# Generated by Django 5.1.4 on 2025-01-16 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_alter_group_class_leader'),
        ('students', '0004_remove_student_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='groups.group'),
        ),
    ]
