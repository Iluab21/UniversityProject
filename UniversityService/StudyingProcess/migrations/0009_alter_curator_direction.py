# Generated by Django 4.1.2 on 2022-11-03 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyingProcess', '0008_alter_curator_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curator',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StudyingProcess.direction'),
        ),
    ]
