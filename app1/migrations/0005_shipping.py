# Generated by Django 4.2.16 on 2024-12-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]