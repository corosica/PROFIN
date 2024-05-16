from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import DepositOptionsSerializer,DepositProductsSerializer
from .models import DepositOptions,DepositProducts
# Create your views here.

@api_view(['GET']) #환전 API
def exchange_calculator(request):
    date = '20240517' # 날자를 params로 받는다
    api_key = settings.EXCHANGE_API_KEY
    api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={date}&data=AP01"
    data = requests.get(api_url)
    count = 0
    while len(data.json()) < 2:
        count+=1
        if count >=10:
            date = "20240514"
        else:
            date = str(int(date)-1)
        api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={date}&data=AP01"
        data = requests.get(api_url)
    return Response(data.json(), status=status.HTTP_200_OK) # 해당 일자의 환율 데이터를 보내준다/ 이후 프론트 측에서 computed + v-models 로 실시간 계산

@api_view(['GET']) 
def deposit_list(request):
    deposit_items = get_list_or_404(DepositProducts)
    serializer = DepositProductsSerializer(deposit_items, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET']) 
def save_deposit_list(request):
    api_key = settings.BANK_API_KEY
    for page in range(1,10):
        api_url = f"https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page}"
        response = requests.get(api_url).json()
        for data in response['result'].get('baseList'):
            serializer = DepositProductsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        for data in response['result'].get('optionList'):
            serializer = DepositOptionsSerializer(data=data)
            if serializer.is_valid():
                serializer.save(product = DepositProducts.objects.get(fin_prdt_cd = data["fin_prdt_cd"]))
    return Response(status=status.HTTP_200_OK,data={'message':'okay'})


@api_view(['GET']) 
def deposit_detail(request,deposit_pk):
    product = get_object_or_404(DepositProducts,pk=deposit_pk)
    options = DepositOptions.objects.filter(fin_prdt_cd = product.fin_prdt_cd)
    serializer = DepositOptionsSerializer(options,many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)