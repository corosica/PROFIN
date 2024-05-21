# accounts/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
 # 필요한 필드들을 추가합니다.
 nickname = serializers.CharField(
 required=False,
 allow_blank=True,
 max_length=255
)
 age = serializers.IntegerField(
    required=False,
 )
 gender = serializers.ChoiceField(
 choices = (
    ('비공개','비공개'),
    ('남성', '남성'),
    ('여성','여성'),
),
 required=False,
 allow_blank=True, )
 asset = serializers.IntegerField(
  required=False,
 )
 job = serializers.CharField(
  required=False,
  allow_blank=True,
  max_length=255,
 )
 goal = serializers.ChoiceField(
  choices=(
     ('무계획','무계획'),
    ('안전형', '안전형'),
    ('수익형','수익형'),),
    required=False,
    allow_blank=True,)
 points = serializers.IntegerField(
   required=False,
   )
 # 해당 필드도 저장 시 함께 사용하도록 설정합니다.
 def get_cleaned_data(self):
    return {
    'username': self.validated_data.get('username', ''),
    'password1': self.validated_data.get('password1', ''),
    'email': self.validated_data.get('email', ''),

    # nickname 필드 추가
    'nickname': self.validated_data.get('nickname', ''),
    'age': self.validated_data.get('age', 0),
    'gender': self.validated_data.get('gender', ''),
    'asset': self.validated_data.get('asset', 0),
    'job': self.validated_data.get('job', ''),
    'goal': self.validated_data.get('goal', ''),
    'points': self.validated_data.get('points', 500),
    }
 
# accounts/serailizers.py
from django.contrib.auth import get_user_model
UserModel = get_user_model()
class CustomUserDetailsSerializer(UserDetailsSerializer):
 class Meta:
    extra_fields = []
    # see https://github.com/iMerica/dj-rest-auth/issues/181
    # UserModel.XYZ causing attribute error while importing other
    # classes from `serializers.py`. So, we need to check whether the auth model has
    # the attribute or not
    if hasattr(UserModel, 'USERNAME_FIELD'):
        extra_fields.append(UserModel.USERNAME_FIELD)
    if hasattr(UserModel, 'EMAIL_FIELD'):
        extra_fields.append(UserModel.EMAIL_FIELD)
    if hasattr(UserModel, 'first_name'):
        extra_fields.append('first_name')
    if hasattr(UserModel, 'last_name'):
        extra_fields.append('last_name')
    if hasattr(UserModel, 'nickname'):
        extra_fields.append('nickname')
    if hasattr(UserModel, 'age'):
        extra_fields.append('age')
    if hasattr(UserModel, 'gender'):
       extra_fields.append('gender')
    if hasattr(UserModel, 'asset'):
       extra_fields.append('asset')
    if hasattr(UserModel, 'job'):
       extra_fields.append('job')
    if hasattr(UserModel, 'goal'):
       extra_fields.append('goal')
    if hasattr(UserModel, 'points'):
       extra_fields.append('points')
    model = UserModel
    fields = ('pk', *extra_fields)
    read_only_fields = ('email',)
