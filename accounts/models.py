from django.db import models

from django.contrib.auth.models import AbstractUser

#test주석
class User(AbstractUser):
    name = models.CharField('이름', max_length=20)
    image = models.ImageField('이미지', null =True, blank = True)
    phoneNumber = models.CharField('전화번호', max_length=13)
    gender = models.CharField('성별', max_length=2)
    role = models.CharField('역할', max_length=2)
    introduction = models.TextField('소개')
    first_name = None #
    last_name = None

