# Generated by Django 2.1.1 on 2020-10-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.BooleanField(default=False)),
                ('q2', models.BooleanField(default=False)),
                ('q3', models.BooleanField(default=False)),
                ('q4', models.BooleanField(default=False)),
            ],
        ),
    ]