# Generated by Django 3.1 on 2021-12-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.IntegerField()),
            ],
            options={
                'db_table': 'test_table',
            },
        ),
    ]