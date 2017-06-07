from django.db import models
#from .car import Car


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    # cars = models.ManyToManyField(
    #     Car,
    #     related_name='%(app_label)s_%(class)ss',
    #     related_query_name='%(app_label)s_%(class)s',
    #     # app_label : 모듈 이름 introduction_to_models
    #     # class : 호출 할 클래스(데이터 모델 클래스) 명의 소문자, student, teacher
    # )


    class Meta:
        abstract = True
        # Meta 옵션 : abstract - 클래스의 추상화.
        # 일반 모델로 사용 할 수 없으며, DB로 생성 할 수 없다.
        #
        # 모델 클래스가 상속받아 모델을 생성할 경우 추상 클래스의 속성을 사용할 수 있다.
        # 모델 DB생성시 공통된 부분을 반복 생성 하지 않기 위한 방법.


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return 'HoneGroup {}\'s student({}, {})'.format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_student'
        # Meta 옵션 : db_table - 테이블 명을 지정 할 수 있음


class Teacher(CommonInfo):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {}\'s teacher ({}, {})'.format(
            self.class_,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_teacher'
