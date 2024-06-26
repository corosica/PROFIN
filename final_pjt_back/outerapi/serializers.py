from rest_framework import serializers
from .models import DepositOptions,DepositProducts,SavingProducts,SavingOptions,BuyDepositProduct,BuySavingProduct,Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'user', 'date']


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class DepositProductsSerializer(serializers.ModelSerializer):
    deposit_options = DepositOptionsSerializer(many=True,read_only=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)

class SavingProductsSerializer(serializers.ModelSerializer):
    saving_options = SavingOptionsSerializer(many=True,read_only=True)
    class Meta:
        model = SavingProducts
        fields = '__all__'

class DepositProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyDepositProduct
        fields = '__all__'

class SavingProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuySavingProduct
        fields = '__all__'