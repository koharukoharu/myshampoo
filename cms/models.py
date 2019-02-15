from django.db import models

# Create your models here.


class Shampoo(models.Model):
    """シャンプー"""
    name = models.CharField('シャンプー名', max_length=255)
    publisher = models.CharField('メーカー', max_length=255, blank=True)
    price = models.IntegerField('値段', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    shampoo = models.ForeignKey(Shampoo, verbose_name='シャンプー', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

