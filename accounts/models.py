from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    #일반 user 생성
    def create_user(self, name, nickname, id, password=None ):
        #이름
        if not name:
            raise ValueError('이름을 입력해주세요.')
        #닉네임
        if not nickname:
            raise ValueError('닉네임 입력해주세요.')
        #아이디
        if not id:
            raise ValueError('아이디를 입력해주세요.')
        #비밀번호
        if not password:
            raise ValueError('비밀번호를 입력해주세요.')

        user = self.model(
            name = name,
            nickname = nickname,
            id = id
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    #관리자 user 생성
    def create_superuser(self, name, nickname, id, password=None):
        user = self.create_user(
            name = name,
            nickname = nickname,
            id = id,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'id'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.id