# Generated by Django 4.2.8 on 2024-05-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('비공개', '비공개'), ('남성', '남성'), ('여성', '여성')], default='비공개', max_length=255),
        ),
    ]