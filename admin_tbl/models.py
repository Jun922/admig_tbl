from django.db import models
from django.core import validators


class Student(models.Model):
    name = models.CharField(
        verbose_name = '名前',
        max_length = 10,
    )

    age = models.IntegerField(
        verbose_name = '年齢',
        validators = [validators.MinValueValidator(1)],
        blank = True,
        null = True,
    )

    sex = models.IntegerField(
        verbose_name = '性別',
        choices = (
            (1, '男性'),
            (2, '女性'),
        ),
        default = 1,
    )

    job = models.CharField(
        verbose_name = "仕事",
        max_length = 15,
    )
    
    memo = models.TextField(
        verbose_name = '備考',
        max_length = 300,
        blank = True,
        null = True,
    )

    created_at = models.DateTimeField(
        verbose_name = '登録日',
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        verbose_name = '更新日',
        auto_now_add = True,
    )

    def __str__(self):
        return self.name
    