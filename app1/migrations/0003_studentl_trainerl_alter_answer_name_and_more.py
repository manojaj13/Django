# Generated by Django 4.2.1 on 2023-05-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slog', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='trainerl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlog', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cname',
            field=models.CharField(max_length=500),
        ),
    ]
