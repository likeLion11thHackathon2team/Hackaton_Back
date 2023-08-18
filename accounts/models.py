from django.db import models

from django.contrib.auth.models import AbstractUser

# class UserManager(BaseUserManager):
#     use_in_migrations = True
#     #user 생성
#     def create_user(self, username, password = None):
#         if not username:
#             raise ValueError('이름을 입력해주세요')
#         user = self.model(
#             username = username
#         )
#         user.set_password(password)
#         user.save(using=self.db)


class User(AbstractUser):
    name = models.CharField('이름', max_length=20)
    image = models.ImageField('이미지', null =True, blank = True)
    phoneNumber = models.CharField('전화번호', max_length=13)
    gender = models.CharField('성별', max_length=2)
    role = models.CharField('역할', max_length=2)
    introduction = models.TextField('소개')
    first_name = None
    last_name = None

    #User 모델 field
    # is_active = models.BooleanField(default = True)
    # is_admin = models.BooleanField(default=False)

    # objects = UserManager()

    def __str__(self):
        return self.username
    
