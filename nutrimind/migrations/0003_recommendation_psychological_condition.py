# Generated by Django 4.2.6 on 2024-09-25 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrimind', '0002_psychologicalcondition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='psychological_condition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nutrimind.psychologicalcondition'),
            preserve_default=False,
        ),
    ]