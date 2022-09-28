# Generated by Django 3.2.6 on 2021-09-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='incharge',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('branch_field', models.CharField(default=None, max_length=30, null=True)),
                ('semester_field', models.CharField(default=None, max_length=10, null=True)),
                ('contact_field', models.CharField(default=None, max_length=10, null=True)),
                ('email_field', models.EmailField(default='', max_length=100)),
            ],
        ),
    ]