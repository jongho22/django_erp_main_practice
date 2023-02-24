# Generated by Django 4.1.5 on 2023-02-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_department_incumbent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incumbent',
            name='개인_이메일',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='경력사항1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='경력사항2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='경력사항3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='경력사항4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='경력사항5',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='근속일',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='비상연락망',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='생년월일',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='어학사항1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='어학사항2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='어학사항3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='어학사항4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='어학사항5',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='연락처',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='입사구분',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='입사일',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='자격사항1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='자격사항2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='자격사항3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='자격사항4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='자격사항5',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='전공',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='주민등록번호',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='주소',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='직책',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='최종학력',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='학교',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='학위',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='학점',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incumbent',
            name='회사_이메일',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
