# Generated by Django 3.1 on 2019-09-22 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0022_add_index'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='testtable',
            name='test_index',
        ),
    ]