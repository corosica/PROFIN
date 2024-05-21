from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

# Create your models here.
GENDER_CHOICES = (
   ('비공개','비공개'),
    ('남성', '남성'),
    ('여성','여성'),
)

GOAL_CHOICES = (
   ('무계획','무계획'),
    ('안전형', '안전형'),
    ('수익형','수익형'),
)

class User(AbstractUser):
    nickname = models.CharField(max_length=255,blank=True)
    age = models.IntegerField(null=True)
    gender = models.fields.CharField(max_length=255,choices=GENDER_CHOICES,default='비공개')
    asset = models.IntegerField(null=True,default=0)
    job = models.CharField(max_length=255,blank=True,default='무직')
    goal = models.CharField(max_length=255,choices=GOAL_CHOICES,default='무계획')

class CustomAccountAdapter(DefaultAccountAdapter):
 def save_user(self, request, user, form, commit=True):
    data = form.cleaned_data
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    username = data.get("username")
    # nickname 필드를 추가
    nickname = data.get("nickname")
    # age 필드를 추가
    age = data.get("age")
    # gender 필드를 추가
    gender = data.get("gender")
    # asset 필드를 추가
    asset = data.get("asset")
    # job 필드를 추가
    job = data.get("job")
    # goal 필드를 추가
    goal = data.get("goal")
    user_email(user, email)
    user_username(user, username)
    if first_name:
        user_field(user, "first_name", first_name)
    if last_name:
        user_field(user, "last_name", last_name)
    if nickname:
        user_field(user, "nickname", nickname)
    else:
        user_field(user, "nickname", username)
    if gender:
        user_field(user, "gender", gender)
    if asset:
        user.asset = asset
    if job:
        user_field(user, "job", job)
    if goal:
        user_field(user, "goal", goal)
    if age:
        user.age = age
    if "password1" in data:
        user.set_password(data["password1"])
    else:
        user.set_unusable_password()
    self.populate_username(request, user)
    if commit:
    # Ability not to commit makes it easier to derive from
    # this adapter by adding
        user.save()
    return user

