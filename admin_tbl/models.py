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

    ability = models.IntegerField(
        verbose_name = '理解力',
        choices = (
            (1, '卒業不可'),
            (2, '及第点'),
            (3, '普通'),
            (4, '優秀'),
            (5, '講師候補'),
        ),
        default = 3,
    )

    graduated = models.BooleanField(
        verbose_name = "卒業ステータス",
        default = False,
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
        return str(self.name)


class Lesson(models.Model):
    name = models.ForeignKey(
        Student,
        on_delete = models.CASCADE
    )
    
    times = models.IntegerField(
        verbose_name = 'レッスン回数',
    )

    progress = models.IntegerField(
        verbose_name = '進捗',
        choices = (
            (0, '---'),
            (1, 'progate初級'),
            (2, 'progate中級'),
            (3, 'progate上級'),
            (4, 'progate道場初級'),
            (5, 'progate道場中級'),
            (6, 'progate道場上級'),
            (7, '1 Profile'),
            (8, '2 PhotoBook'),
            (9, '3 PhotoBook2'),
            (10, '4 Recipe前半'),
            (11, '5 Recipe後半'),
            (12, '6 WoodenJewelry'),
            (13, '7 MyWork'),
            (14, '8 Meg88'),
            (15, '9 Totally'),
            (16, '10 WED'),
            (17, '11 TravelBlog'),
            (18, '12 創作'),
            (19, '13 Coffee'),
            (20, '14 FurnitureDesign'),
            (21, '15 明るいHouse'),
            (22, '16 Sneakers'),
            (23, '17 BBB英会話'),
            (24, 'WordPress'),
            (25, 'オリジナルサイト'),
            (26, '案件獲得'),
        ),
        default = 0,
    )
    
    memo = models.TextField(
        verbose_name = '備考',
        max_length = 500,
        blank = True,
        null = True,
    )

    def __str__(self):
        return str(self.name)
    