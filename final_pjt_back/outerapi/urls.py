from django.urls import path
from . import views
from .views import AttendanceView


urlpatterns = [
    path('exchange/', views.exchange_calculator), # 환율 계산 API
    path('deposit/', views.deposit_list), # 예적금 리스트 API 
    path('deposit/saving/', views.save_deposit_list), # 예적금 리스트 API 
    path('deposit/<int:deposit_pk>/', views.deposit_detail), # 예적금 상세 API
    path('deposit/<int:deposit_pk>/<int:option_pk>/', views.buy_deposit), # 예금 상품 구매 해제 API
    path('saving/', views.saving_list), # 적금 리스트 API 
    path('saving/saving/', views.save_saving_product), # 적금 리스트 API 
    path('saving/<int:deposit_pk>/', views.saving_detail), # 적금 상세 API
    path('saving/<int:saving_pk>/<int:option_pk>/', views.buy_saving), # 적금 상품 구매 해제 API
    path('search_deposit/', views.search_deposits), # 적금 상품 구매 해제 API
    path('kakaomaps/', views.find_bank), # 은행 찾기 kakaomap
    path('recommend/normal/', views.normal_recommend), # 일반 추천
    path('recommend/premium/', views.premium_recommend), # 프리미엄 추천 
    path('attendance/', AttendanceView.as_view(), name='attendance'),
    path('check_user/<str:username>/', views.check_user), # 유저 체크 

]
