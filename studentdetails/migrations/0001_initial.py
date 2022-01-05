# Generated by Django 3.2.7 on 2021-10-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('department', models.TextField()),
                ('mobile', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('qualification', models.TextField()),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=75)),
                ('mobile', models.IntegerField()),
                ('department', models.TextField()),
                ('father_name', models.TextField()),
                ('ssc_marks', models.IntegerField()),
                ('inter_marks', models.IntegerField()),
                ('roll_number', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
