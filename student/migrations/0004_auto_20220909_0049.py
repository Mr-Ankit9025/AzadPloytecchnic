# Generated by Django 3.2.7 on 2022-09-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_mycourse_hodpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
                ('clogo', models.ImageField(upload_to='static/company')),
            ],
        ),
        migrations.DeleteModel(
            name='placement',
        ),
    ]
