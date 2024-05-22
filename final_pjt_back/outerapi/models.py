from django.db import models
from django.conf import settings

class Exchange(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    exchange_rate = models.FloatField()
    base_date = models.DateField()

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    buy_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='buy_deposit_products', through='BuyDepositProduct')
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    max_limit = models.IntegerField(null=True)
    dcls_strt_day = models.CharField(max_length=50)

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='deposit_options')
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    buy_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='buy_saving_products', through='BuySavingProduct')
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    max_limit = models.IntegerField(null=True)
    dcls_strt_day = models.CharField(max_length=50)

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, related_name='saving_options')
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
    rsrv_type_nm = models.CharField(max_length=50)

class BuyDepositProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    options = models.ForeignKey(DepositOptions, on_delete=models.CASCADE, null=True)

class BuySavingProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    options = models.ForeignKey(SavingOptions, on_delete=models.CASCADE, null=True)
