from django.urls import path
from . import views


urlpatterns = [
    path('exchange/', views.exchange_calculator), # 환율 계산 API
    path('deposit/', views.deposit_list), # 예적금 리스트 API 

]
