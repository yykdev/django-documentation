from django.db import models

class ManuFacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(
        # ManuFacturer, # 먼저 선언 되는 클래스 사용시
        # 'ManuFacturer', # 아직 정의 되지 않은 클래스 사용시
        # 'myapp.ManuFacturer' # 다른 모듈의 클래스 사용시
        ManuFacturer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name