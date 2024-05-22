from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='asset',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('비공개', '비공개'), ('남성', '남성'), ('여성', '여성')], default='비공개', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='goal',
            field=models.CharField(choices=[('무계획', '무계획'), ('안전형', '안전형'), ('수익형', '수익형')], default='무계획', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, default='무직', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=500),
        ),
    ]
