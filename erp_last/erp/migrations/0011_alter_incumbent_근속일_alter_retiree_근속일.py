# Generated by Django 4.1.5 on 2023-02-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0010_alter_incumbent_팀_alter_retiree_팀'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incumbent',
            name='근속일',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retiree',
            name='근속일',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
