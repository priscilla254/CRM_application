# Generated by Django 4.0.2 on 2022-02-22 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_delete_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('Company', models.CharField(max_length=80)),
                ('company_position', models.CharField(max_length=80)),
                ('phone_number', models.IntegerField(default=0)),
                ('email_address', models.EmailField(max_length=254)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.agent')),
            ],
        ),
    ]