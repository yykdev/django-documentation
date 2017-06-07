from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('student', '학생'),
        ('teacher', '선생'),
    )

    person_type = models.CharField(
        '유형',
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0]
    )
    # teacher속성 지정 (ForeignKey, 'self'를 이용해 자기 자신을 가리킴, null=True허용)
    teacher = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        '셔츠사이즈',
        max_length=1,
        choices=SHIRT_SIZES,
        help_text='남자는 L쓰세요',
    )

    def __str__(self):
        return self.name

# INSTALLED_APPS에 이 모델이 속하는 app추가
# makemigrations로 migrations생성
# migrate로 migration을 적용
# admin.py에 Person클래스 등록
# createsuperuser로 슈퍼유저 계정 생성
# runserver후 admin접속해서 Person객체 생성 및 저장해보기
