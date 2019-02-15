from django.forms import ModelForm
from cms.models import Shampoo


class ShampooForm(ModelForm):
    """シャンプーのフォーム"""
    class Meta:
        model = Shampoo
        fields = ('name', 'publisher', 'price',)

