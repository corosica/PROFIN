from django.db import models

# Create your models here.

class Exchange(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    exchange_rate = models.FloatField()
    base_date = models.DateField()


class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm =  models.TextField()
    etc_note  =  models.TextField()
    join_deny = models.IntegerField() 
    join_member  =  models.TextField()
    join_way =  models.TextField()
    spcl_cnd =  models.TextField()

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField() 
    intr_rate_type_nm = models.CharField(max_length=100) 
    intr_rate = models.FloatField() 
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField() 


'''
{
"result": 1,
"cur_unit": "IDR(100)",
"ttb": "8.43",
"tts": "8.6",
"deal_bas_r": "8.52",
"bkpr": "8",
"yy_efee_r": "0",
"ten_dd_efee_r": "0",
"kftc_bkpr": "8",
"kftc_deal_bas_r": "8.52",
"cur_nm": "인도네시아 루피아"
},
{
"result": 1,
"cur_unit": "JPY(100)",
"ttb": "868.18",
"tts": "885.71",
"deal_bas_r": "876.95",
"bkpr": "876",
"yy_efee_r": "0",
"ten_dd_efee_r": "0",
"kftc_bkpr": "876",
"kftc_deal_bas_r": "876.95",
"cur_nm": "일본 옌"

'''