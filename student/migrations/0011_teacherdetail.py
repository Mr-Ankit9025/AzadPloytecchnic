# Generated by Django 3.2.7 on 2022-11-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_delete_teachdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacherDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.CharField(max_length=50)),
                ('teacherPosition', models.CharField(max_length=50)),
                ('teacherPhoto', models.ImageField(null=True, upload_to='static/teacherPhoto')),
                ('aboutTeacher', models.TextField()),
            ],
        ),
    ]
