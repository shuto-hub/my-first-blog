# Generated by Django 2.2.5 on 2019-09-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190909_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data1',
            field=models.IntegerField(choices=[(1, 'E'), (2, 'D'), (3, 'C'), (4, 'B'), (5, 'A')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='data2',
            field=models.IntegerField(choices=[(1, 'E'), (2, 'D'), (3, 'C'), (4, 'B'), (5, 'A')], null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='data3',
            field=models.IntegerField(choices=[(1, 'E'), (2, 'D'), (3, 'C'), (4, 'B'), (5, 'A')], null=True),
        ),
    ]