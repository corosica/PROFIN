from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=255,blank=True)
    age = models.IntegerField(null=True)
class CustomAccountAdapter(DefaultAccountAdapter):
 def save_user(self, request, user, form, commit=True):
    data = form.cleaned_data
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    username = data.get("username")
    # nickname 필드를 추가
    nickname = data.get("nickname")
    # nickname 필드를 추가
    age = data.get("age")
    user_email(user, email)
    user_username(user, username)
    if first_name:
        user_field(user, "first_name", first_name)
    if last_name:
        user_field(user, "last_name", last_name)
    if nickname:
        user_field(user, "nickname", nickname)
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

