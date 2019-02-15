from django.forms import ModelForm
from cms.models import Shampoo, Impression


class ShampooForm(ModelForm):
    """シャンプーのフォーム"""
    class Meta:
        model = Shampoo
        fields = ('name', 'publisher', 'price',)


class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment',)

