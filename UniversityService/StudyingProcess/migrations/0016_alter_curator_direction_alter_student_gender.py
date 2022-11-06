# Generated by Django 4.1.2 on 2022-11-03 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyingProcess', '0015_alter_curator_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curator',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudyingProcess.direction'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, verbose_name='Gender'),
        ),
    ]
