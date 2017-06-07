from django.db import models

class TimeStampedMixin(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    # auto_now_add 객체가 생성될 때 시간 저장
    modified_date = models.DateTimeField(auto_now=True)
    # auto_now 객체 생성 후 데이터가 업데이트 될 때 사용

    class Meta:
        abstract = True