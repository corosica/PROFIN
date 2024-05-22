from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import DepositOptionsSerializer,DepositProductsSerializer,SavingOptionsSerializer,SavingProductsSerializer,DepositProductListSerializer,SavingProductListSerializer
from .models import DepositOptions,DepositProducts,SavingOptions,SavingProducts,BuyDepositProduct,BuySavingProduct
# Create your views here.
from datetime import datetime


@api_view(['GET']) #환전 API
def exchange_calculator(request):
    date = datetime.now().strftime("%Y%m%d") # 날자를 오늘 날자로 받는다
    api_key = settings.EXCHANGE_API_KEY
    api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={date}&data=AP01"
    data = requests.get(api_url)
    count = 0
    print(data.json(),count)
    while len(data.json()) < 2:
        count+=1
        print('hi')
        if count >=10:
            date = "20240514"
        else:
            date = str(int(date)-1)
        api_url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={date}&data=AP01"
        data = requests.get(api_url)
        print(data.json())
    return Response(data.json(), status=status.HTTP_200_OK) # 해당 일자의 환율 데이터를 보내준다/ 이후 프론트 측에서 computed + v-models 로 실시간 계산

@api_view(['GET']) 
def deposit_list(request):
    deposit_items = get_list_or_404(DepositProducts)
    serializer = DepositProductsSerializer(deposit_items, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET']) 
def save_deposit_list(request):
    api_key = settings.BANK_API_KEY
    for page in range(1,2):
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
def save_saving_product(request):
    api_key = settings.BANK_API_KEY
    for page in range(1,2):
        api_url = f"https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={page}"
        response = requests.get(api_url).json()
        for data in response['result'].get('baseList'):
            serializer = SavingProductsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        for data in response['result'].get('optionList'):
            serializer = SavingOptionsSerializer(data=data)
            if serializer.is_valid():
                serializer.save(product = SavingProducts.objects.get(fin_prdt_cd = data["fin_prdt_cd"]))
    return Response(status=status.HTTP_200_OK,data={'message':'okay'})

@api_view(['GET']) 
def saving_list(request):
    saving_items = get_list_or_404(SavingProducts)
    serializer = SavingProductsSerializer(saving_items, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET']) 
def saving_detail(request,deposit_pk):
    product = get_object_or_404(SavingProducts,pk=deposit_pk)
    return Response(SavingProductsSerializer(product).data,status=status.HTTP_200_OK)

@api_view(['GET']) 
def deposit_detail(request,deposit_pk):
    product = get_object_or_404(DepositProducts,pk=deposit_pk)
    return Response(DepositProductsSerializer(product).data,status=status.HTTP_200_OK)

@api_view(['POST']) 
def find_bank(request):
    city = request.data.get('city')
    gu = request.data.get('gu')
    bank = request.data.get('bank')

    api_key = f'KakaoAK {settings.KAKAO_REST_API_KEY}'
    api_url1 = f"https://dapi.kakao.com/v2/local/search/address.json?analyze_type=similar&page=1&size=10&query={city}+{gu}"
    data = requests.get(api_url1,headers={'Authorization' : api_key}).json()
    x = data['documents'][0]['address']['x']
    y = data['documents'][0]['address']['y']

    api_url2 = f"https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy&x={x}&y={y}&radius=4000&query={bank}&category_group_code=BK9"
    api_url3 = f"https://dapi.kakao.com/v2/local/search/keyword.json?page=2&size=15&sort=accuracy&x={x}&y={y}&radius=4000&query={bank}&category_group_code=BK9"

    response = requests.get(api_url2,headers={'Authorization' : api_key}).json()
    if len(response['documents']) >= 15:
        response2 = requests.get(api_url3,headers={'Authorization' : api_key}).json()
        response['documents'].extend(response2['documents'])
    response['meta']['x'] = x
    response['meta']['y'] = y

    return Response(response,status=status.HTTP_200_OK)

@api_view(['POST']) 
def buy_deposit(request,deposit_pk,option_pk):
    product = get_object_or_404(DepositProducts,pk=deposit_pk)
    option = get_object_or_404(DepositOptions,pk=option_pk)
    if request.user in product.buy_user.all():
        product.buy_user.remove(request.user)
        return Response(status=status.HTTP_200_OK)
    else:
        BuyDepositProduct.objects.create(user=request.user, product=product, intr_rate=option.intr_rate, intr_rate2=option.intr_rate2)
        return Response(status=status.HTTP_200_OK)

@api_view(['POST']) 
def buy_saving(request,saving_pk,option_pk):
    product = get_object_or_404(SavingProducts,pk=saving_pk)
    option = get_object_or_404(SavingOptions,pk=option_pk)
    if request.user in product.buy_user.all():
        product.buy_user.remove(request.user)
        return Response(status=status.HTTP_200_OK)
    else:
        BuySavingProduct.objects.create(user=request.user, product=product, intr_rate=option.intr_rate, intr_rate2=option.intr_rate2)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET']) 
def search_deposits(request):
    deposit_products = get_list_or_404(BuyDepositProduct,user=request.user)
    saving_products = get_list_or_404(BuySavingProduct,user=request.user)
    return Response({'예금':DepositProductListSerializer(deposit_products,many=True).data,'적금':SavingProductListSerializer(saving_products,many=True).data},status=status.HTTP_200_OK)

@api_view(['GET']) 
def normal_recommend(request):
    # 사용자의 나이를 얻어옵니다. 여기서는 request.user.profile.age를 가정합니다.
    user_age = request.user.age

    # saving_items와 deposit_items를 가져옵니다.
    saving_items = get_list_or_404(BuySavingProduct)
    deposit_items = get_list_or_404(BuyDepositProduct)

    # 딕셔너리를 사용하여 가중치를 계산합니다.
    weighted_items = {}

    def add_weight(item, user_age):
        if abs(item.user.age - user_age) <= 1: 
            weight = 2.0 
        elif abs(item.user.age - user_age) <= 5:
            weight = 1.0
        else:
            weight = 0.1
        if item.product.fin_prdt_nm in weighted_items:
            weighted_items[item.product.fin_prdt_nm]['weight'] += weight
        else:
            weighted_items[item.product.fin_prdt_nm] = {
                'item': item,
                'weight': weight
            }

    # saving_items와 deposit_items의 가중치를 계산하여 딕셔너리에 추가합니다.
    for item in saving_items:
        add_weight(item, user_age)

    for item in deposit_items:
        add_weight(item, user_age)

    # 가중치에 따라 항목을 정렬합니다.
    sorted_items = sorted(weighted_items.values(), key=lambda x: x['weight'], reverse=True)

    # 상위 5개 항목을 선택합니다.
    top_5_items = sorted_items[:5]

    # 반환할 데이터를 구성합니다.
    result = [
        {
            "id": item['item'].product.id,
            "name": item['item'].product.fin_prdt_nm,
            "type": "적금" if isinstance(item['item'], BuySavingProduct) else "예금",
            "weight": item['weight']
        }
    for item in top_5_items]

    return Response(data=result, status=status.HTTP_200_OK)
@api_view(['GET'])
def premium_recommend(request):
    print(request.user.age)
    saving_items = get_list_or_404(BuySavingProduct)
    print(request.user.age)
    '''
    request.user.goal : 안전형 or 수익형 or 무계획(안전형과 수익형의 평균, 인원수의 가중치를 더 많이 받음)
    request.user.age : 현재 나이, 비슷한 나이대 인원
    '''
    return Response('h', status=status.HTTP_200_OK)
