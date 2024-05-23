from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import DepositOptionsSerializer,DepositProductsSerializer,SavingOptionsSerializer,SavingProductsSerializer,DepositProductListSerializer,SavingProductListSerializer
from .models import DepositOptions,DepositProducts,SavingOptions,SavingProducts,BuyDepositProduct,BuySavingProduct
# Create your views here.
from datetime import datetime

from django.utils import timezone
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model  # 추가: 사용자 모델 가져오기

class AttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        today = timezone.now().date()

        # Check if the user has already checked in today
        if Attendance.objects.filter(user=user, date=today).exists():
            return Response({"message": "이미 오늘은 출석체크를 하셨습니다."}, status=status.HTTP_400_BAD_REQUEST)

        attendance = Attendance(user=user, date=today)
        attendance.save()
        user.points = user.points + 50
        user.save()
        return Response({"message": f"출석체크 되었습니다. \n현재 포인트{user.points}"}, status=status.HTTP_201_CREATED)


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
    deposit_products = BuyDepositProduct.objects.filter(user=request.user)
    saving_products = BuySavingProduct.objects.filter(user=request.user)
    return Response({'예금':DepositProductListSerializer(deposit_products,many=True).data,'적금':SavingProductListSerializer(saving_products,many=True).data},status=status.HTTP_200_OK)

@api_view(['GET']) 
def normal_recommend(request):
    if request.user.points < 100:
        return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
    
    # 사용자의 나이를 얻어옵니다. 여기서는 request.user.profile.age를 가정합니다.
    user_age = request.user.age
    request.user.points = request.user.points - 100
    request.user.save()

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
    print(request.user.points)
    if request.user.points < 3000:
        return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
    
    request.user.points = request.user.points - 3000
    request.user.save()
    #유저의 나이를 받는다
    user_age = request.user.age
    # 순회를 돌기 위한 deposit_option과 saving_option을 가져욘다
    deposit_options = get_list_or_404(DepositOptions)
    saving_options = get_list_or_404(SavingOptions)
    max_people = 0
    result = []
    protect_list = []
    profit_list = []
    default_list = []
    money = request.user.asset*10000
    for item in deposit_options: # 예금
        if  item.product.max_limit != None and money > item.product.max_limit:
            continue # 한도초과 고려안하기
        people1 = item.product.buy_user.filter(age__range=(user_age-1,user_age+1)).count()
        people2 = item.product.buy_user.filter(age__range=(user_age-5,user_age+5)).count()
        people3 = item.product.buy_user.count() +0.0000001
        if item.save_trm <= 12: # 중단기
            protect = 0.6
            profit = 0.4
        else: # 장기
            protect = 0.4
            profit = 0.6
        protect = protect * item.intr_rate * 0.5
        protect = protect * 0.2 /(1+(item.intr_rate2 - item.intr_rate))
        profit = profit * item.intr_rate2 * 0.4
        profit = profit * 0.2 # 자유적립식/정액적립식(예금*)
        if item.intr_rate_type_nm == '단리':
            profit = profit * 0.2
        else:
            profit = profit * 0.3

        default = 0.5 * protect + 0.5 * profit

        # 위는 인원수 제외 가중치 밑은 인원수 가중치 계산
        people = (people1*2 + (people2-people1)*1.5 + (people3-people2)*0.01)/people3
        if people > max_people: 
            max_people = people
        protect_list.append([protect, people,'예금',item.product.kor_co_nm,item.product.fin_prdt_nm,item.product.id,item.id,item.intr_rate,item.intr_rate2,item.save_trm]) 
        profit_list.append([profit, people,'예금',item.product.kor_co_nm,item.product.fin_prdt_nm,item.product.id,item.id,item.intr_rate,item.intr_rate2,item.save_trm]) 
        default_list.append([default, people,'예금',item.product.kor_co_nm,item.product.fin_prdt_nm,item.product.id,item.id,item.intr_rate,item.intr_rate2,item.save_trm]) 

        # 가중치 , 인원 가중치 , 예금 적금 종류, 은행명, 상품명, 상품코드, 옵션코드


    for item in saving_options: # 적금
        if  item.product.max_limit != None and money > item.product.max_limit:
            continue # 한도초과 고려안하기
        people1 = item.product.buy_user.filter(age__range=(user_age-1,user_age+1)).count()
        people2 = item.product.buy_user.filter(age__range=(user_age-5,user_age+5)).count()
        people3 = item.product.buy_user.count() +0.0000001
        if item.save_trm <= 12: # 중단기
            protect = 0.6
            profit = 0.4
        else: # 장기
            protect = 0.4
            profit = 0.6
        protect = protect * item.intr_rate * 0.5
        protect = protect * 0.2 /(1+(item.intr_rate2 - item.intr_rate))
        profit = profit * item.intr_rate2 * 0.4
        profit = profit * 0.2 # 자유적립식/정액적립식(예금*)
        if item.rsrv_type_nm == '자유적립식':
            profit = profit * 0.3 # 자유적립식/정액적립식(예금*)
        else:
            profit = profit * 0.3 # 자유적립식/정액적립식(예금*)
        if item.intr_rate_type_nm == '단리':
            profit = profit * 0.2
        else:
            profit = profit * 0.3

        default = 0.5 * protect + 0.5 * profit

        # 위는 인원수 제외 가중치 밑은 인원수 가중치 계산
        people = (people1*2 + (people2-people1)*1.5 + (people3-people2)*0.01)/people3
        if people > max_people: 
            max_people = people
        protect_list.append([protect, people,'적금',item.product.kor_co_nm,item.product.fin_prdt_nm,item.product.id,item.id,item.intr_rate,item.intr_rate2,item.save_trm]) 
        profit_list.append([profit, people,'적금',item.product.kor_co_nm,item.product.fin_prdt_nm,item.product.id,item.id,item.intr_rate,item.intr_rate2,item.save_trm]) 
        default_list.append([default, people,'적금',item.product.kor_co_nm,item.product.fin_prdt_nm,item.product.id,item.id,item.intr_rate,item.intr_rate2,item.save_trm])
            # 가중치 , 인원 가중치 , 예금 적금 종류, 은행명, 상품명, 상품코드, 옵션코드

    print(request.user.goal)
    people_level = 0.1
    if request.user.goal == '안전형':
        calculate_list = protect_list 
    elif request.user.goal == '수익형':
        calculate_list = profit_list 
    else:
        calculate_list = default_list
        people_level = 0.4 # 사람 수의 가중치를 더 많이 받음
    
    for current_item in calculate_list:
        weight = current_item[0]*(1+people_level*(current_item[1]/max_people))
        result.append({'weight':weight,'type':current_item[2],'bank':current_item[3],'product_name':current_item[4],'product_code':current_item[5],'option_code':current_item[6],'intr_rate':current_item[7],'intr_rate2':current_item[8],'save_trm':current_item[9]})
    sorted_items = sorted(result, key=lambda x: x['weight'], reverse=True)


        

    
    '''
    request.user.goal : 안전형 or 수익형 or 무계획(안전형과 수익형의 평균, 인원수의 가중치를 더 많이 받음)
    request.user.age : 현재 나이, 비슷한 나이대 인원
    item => saving/deposit_items 의 for문으로 돈 요소 (option/product)

    option
    item.intr_rate : 최소 이자율 (float)
    item.intr_rate2 : 최대 이자율 (float)
    item.intr_rate_type_nm : 단리 복리
    item.save_trm : 가입 기간
    item.product => product


    product
    item.id => 아이디
    item.buy_user.count() => 가입한 모든 유저 수
    item.kor_co_nm => 은행명
    item.fin_prdt_nm => 상품명
    item.max_limit => 한도


    단기 장기 기준 : 6개월까지는 단기
    옵션으로 추천해줌
    비율 설정 요약
    - 안전형: 중기(단기) 선호, 최소 이자율 중시, 변동성 낮음
    - 단기/장기: 0.6/0.4
    - 이자율(최소): 0.5 * 이자율
    - 변동성: 0.2 * 변동성 점수=   1/ (1+(최대 이자율−최소 이자율)) (차이 없으면 1, 변동성 낮음,  차이있으면 점점 변동성이 커짐,추천도 낮아짐)
                            


    - 수익형: 장기 선호, 최대 이자율 중시, 자유 적립식 선호, 복리 선호
    - 단기/장기: 0.4/0.6
    - 이자율(최대): 0.4 (전체적으로 최대 이자율 높음)
    - 자유 적립식/정액 적립식(or 예금): 0.3/0.2
    - 단리/복리: 0.2/0.3

    - 무계획 : 안전형과 수익형의 평균, 인원수의 가중치를 더 많이 받음 ( 안전형의 영향을 더 많이 받게 설정)


    - 가입한 인원수에 대한 가중치 

    - 안전형/수익형 
     
    
    '''
    return Response(sorted_items[:10], status=status.HTTP_200_OK)

@api_view(['GET'])
def check_user(request,username):
    print(username)
    user = get_user_model().objects.filter(username=username)
    if len(user) == 1:
        return Response(data = {'ans' :'Yes'},status=status.HTTP_200_OK)
    else:
        return Response(data = {'ans' :'No'},status=status.HTTP_200_OK)