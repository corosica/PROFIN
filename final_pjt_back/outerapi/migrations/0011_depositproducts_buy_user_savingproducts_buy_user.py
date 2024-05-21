# Generated by Django 4.2.8 on 2024-05-21 23:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outerapi', '0010_alter_savingoptions_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositproducts',
            name='buy_user',
            field=models.ManyToManyField(related_name='buy_deposit_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='savingproducts',
            name='buy_user',
            field=models.ManyToManyField(related_name='buy_saving_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
