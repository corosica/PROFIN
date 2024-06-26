# Generated by Django 4.2.8 on 2024-05-22 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outerapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyDepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BuySavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.CharField(max_length=50)),
                ('buy_user', models.ManyToManyField(related_name='buy_saving_products', through='outerapi.BuySavingProduct', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('rsrv_type_nm', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_options', to='outerapi.savingproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.CharField(max_length=50)),
                ('buy_user', models.ManyToManyField(related_name='buy_deposit_products', through='outerapi.BuyDepositProduct', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='outerapi.depositproducts')),
            ],
        ),
        migrations.AddField(
            model_name='buysavingproduct',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='outerapi.savingoptions'),
        ),
        migrations.AddField(
            model_name='buysavingproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outerapi.savingproducts'),
        ),
        migrations.AddField(
            model_name='buysavingproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buydepositproduct',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='outerapi.depositoptions'),
        ),
        migrations.AddField(
            model_name='buydepositproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outerapi.depositproducts'),
        ),
        migrations.AddField(
            model_name='buydepositproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
