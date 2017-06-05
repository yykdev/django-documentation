from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # 자신이 가지고 있는 토핑목록을 뒤에 출력
        # ex) 치즈피자(치즈 토마토)
        #
        # for문 방식. 파이썬 스럽지 않다.
        # topping_string = ''
        # for topping in self.toppings.all():
        #     topping_string += topping.name
        #     topping_string += ', '
        #
        # # 마지막의 두번째 글자를 잘라낸다 ( slice 연산 )
        # # [:-2] 처음 부터 뒤에서 두번째 이전 까지
        # topping_string = topping_string[:-2]


        # join, 리스트 컴프리헨션을 사용하여 한줄로 작성 한다.
        return '{} ( {} )'.format(
            self.name,
            ','.join([ topping.name for topping in self.toppings.all() ])
        )

    class Meta:
        ordering = ('name',)
