from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

# INSTALLED_APPS에 이 모델이 속하는 app추가
# makemigrations로 migrations생성
# admin.py에 Person클래스 등록
# createsuperuser로 슈퍼유저 계정 생성
# runserver 후 admin 접속해서 Person객체 생성 및 저장 해보기