from django.db import models


class CommonInfo2(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ('-name',)
        db_table = 'introduction_to_models_mti_CommonInfo2'


class Student2(CommonInfo2):
    home_group = models.CharField(max_length=5)
    extra_info = models.ForeignKey(
        CommonInfo2,
        related_name='extra_students',
        null=True,
        blank=True,
    )

    def __str__(self):
        return 'HoneGroup {}\'s student({}, {})'.format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_mti_student2'
        # Meta 옵션 : db_table - 테이블 명을 지정 할 수 있음


class Teacher2(CommonInfo2):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {}\'s teacher ({}, {})'.format(
            self.cls,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_mti_teacher2'
