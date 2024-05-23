# Generated by Django 4.2.8 on 2024-05-23 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_qnacomment_qnaarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qnacomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.qnaarticle'),
        ),
    ]
