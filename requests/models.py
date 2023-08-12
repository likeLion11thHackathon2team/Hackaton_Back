from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Request(models.Model):
    category = models.CharField('요청 종류', max_length=4)
    content = models.TextField('요청 내용', blank=True)
    mentiLatitude = models.DecimalField('멘티 위도', max_digits=23, decimal_places=20)
    mentiLongitude = models.DecimalField('멘티 경도', max_digits=24, decimal_places=20)
    mentoLatitude = models.DecimalField('멘토 위도', max_digits=23, decimal_places=20, default=0)
    mentoLongitude = models.DecimalField('멘토 경도', max_digits=23, decimal_places=20, default=0)
    menti = models.ForeignKey(to=User, related_name='mentis', on_delete=models.CASCADE)
    mento = models.ForeignKey(to=User, related_name='mentos', on_delete=models.CASCADE, null=True, blank=True)
    requestTime = models.DateTimeField('요청시간', auto_now_add=True)
    acceptTime = models.DateTimeField('수락시간', auto_now = False , auto_now_add = False, null=True, blank=True)





#######시간되면 후기 작성#######

# class Review(models.Model):
#     rate = models.IntegerField('평점(0.5~5)')
#     content = models.TextField('후기')
#     request = models.OneToOneField(to="Request", on_delete=models.CASCADE)
