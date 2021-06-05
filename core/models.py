from django.db import models


class Plant(models.Model):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

    SIZES = (
        (SMALL, 'Маленький'),
        (MEDIUM, 'Средний'),
        (LARGE, 'Большой'),
    )

    title = models.CharField('название', max_length=255)
    color = models.CharField('цвет', max_length=255)
    size = models.PositiveSmallIntegerField('размер', choices=SIZES)
    area = models.CharField('Место произростания', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.color} {self.title}'

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'
