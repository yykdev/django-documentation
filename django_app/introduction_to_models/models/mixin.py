from django.db import models
from utils.models.mixins import TimeStampedMixin

"""
Post 모델
    author = User와 연결
    title
    content
    created_date : DateTimeField 사용
    modified_date : DateTimeField 사용

Comment 모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date

User 모델
    name
    created_date
    modified_date
"""





class Post(TimeStampedMixin):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(TimeStampedMixin):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    content = models.TextField()

class User(TimeStampedMixin):
    name = models.CharField(max_length=20)