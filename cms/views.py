from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Shampoo
from cms.forms import ShampooForm



# Create your views here.


def shampoo_list(request):
    """シャンプーの一覧"""
 #   return HttpResponse('シャンプーの一覧')
    shampoos = Shampoo.objects.all().order_by('id')
    return render(request,
                    'cms/shampoo_list.html',
                    {'shampoos': shampoos})


def shampoo_edit(request, shampoo_id=None):
    """シャンプーの編集"""
#    return HttpResponse('シャンプーの編集')
    if shampoo_id:
        shampoo = get_object_or_404(Shampoo, pk=shampoo_id)
    else:
        shampoo = Shampoo()

    if request.method == 'POST':
        form = ShampooForm(request.POST, instance=shampoo)
        if form.is_valid():
            shampoo = form.save(commit=False)
            shampoo.save()
            return redirect('cms:shampoo_list')
    else:
        form = ShampooForm(instance=shampoo)

    return render(request, 'cms/shampoo_edit.html', dict(form=form, shampoo_id=shampoo_id))


def shampoo_del(request, shampoo_id):
    """シャンプーの削除"""
    return HttpResponse('シャンプーの削除')
