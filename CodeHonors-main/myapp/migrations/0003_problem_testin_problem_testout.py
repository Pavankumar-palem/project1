# Generated by Django 4.1.1 on 2022-12-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_p_desc_problem_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='testin',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='testout',
            field=models.TextField(default=''),
        ),
    ]