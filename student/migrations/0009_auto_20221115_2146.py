# Generated by Django 3.2.7 on 2022-11-15 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_teachdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachdetail',
            old_name='tdetail',
            new_name='teacherName',
        ),
        migrations.RenameField(
            model_name='teachdetail',
            old_name='tname',
            new_name='teacherPosition',
        ),
        migrations.AddField(
            model_name='teachdetail',
            name='aboutTeacher',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachdetail',
            name='teacherPhoto',
            field=models.ImageField(null=True, upload_to='static/OwnerPic'),
        ),
    ]
