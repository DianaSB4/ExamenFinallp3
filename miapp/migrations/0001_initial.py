# Generated by Django 3.1.4 on 2021-02-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150)),
                ('name', models.TextField(max_length=150)),
                ('hour', models.IntegerField(max_length=3)),
                ('credits', models.IntegerField(max_length=2)),
                ('state', models.CharField(max_length=150)),
            ],
        ),
    ]
