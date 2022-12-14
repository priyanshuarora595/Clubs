# Generated by Django 3.2.6 on 2021-09-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=30, null=True)),
                ('semester', models.CharField(max_length=10, null=True)),
                ('contact_number', models.CharField(max_length=10, null=True)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
    ]
