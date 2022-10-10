# Generated by Django 4.1.2 on 2022-10-07 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stage_name', models.CharField(max_length=255, unique=True)),
                ('Social_link_field', models.URLField(blank=True)),
            ],
            options={
                'ordering': ('Stage_name',),
            },
        ),
    ]