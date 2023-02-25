# Generated by Django 4.1.1 on 2022-09-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=30)),
                ('Mobile', models.CharField(max_length=20)),
                ('Msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('CompanyName', models.CharField(max_length=200)),
                ('Session', models.CharField(max_length=200)),
                ('Branch', models.CharField(max_length=200)),
                ('Image', models.ImageField(default='', upload_to='static/placeimage/')),
            ],
        ),
        migrations.CreateModel(
            name='ugallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdes', models.CharField(max_length=200)),
                ('picture', models.ImageField(default='', upload_to='static/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='uregister',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Rollno', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Smobile', models.CharField(max_length=10)),
                ('Course', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=10)),
                ('Date', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=200)),
                ('Gmobile', models.CharField(max_length=20)),
                ('Image', models.ImageField(null=True, upload_to='static/pimage/')),
            ],
        ),
    ]