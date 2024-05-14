from django.db import models

# Create your models here.

class Exchange(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    exchange_rate = models.FloatField()
    base_date = models.DateField()


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