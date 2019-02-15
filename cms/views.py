from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Shampoo, Impression
from cms.forms import ShampooForm, ImpressionForm

from django.views.generic.list import ListView

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
 #   return HttpResponse('シャンプーの削除')
    shampoo = get_object_or_404(Shampoo, pk=shampoo_id)
    shampoo.delete()
    return redirect('cms:shampoo_list')


class ImpressionList(ListView):
    """感想の一覧"""
    context_object_name = 'impressions'
    template_name = 'cms/impression_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        shampoo = get_object_or_404(Shampoo, pk=kwargs['shampoo_id'])
        impressions = shampoo.impressions.all().order_by('id')
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, shampoo=shampoo)
        return self.render_to_response(context)


def impression_edit(request, shampoo_id, impression_id=None):
    """感想の編集"""
    shampoo = get_object_or_404(Shampoo, pk=shampoo_id)
    if impression_id:
        impression = get_object_or_404(Impression, pk=impression_id)
    else:
        impression = Impression()
    
    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)
        if form.is_valid():
            impression = form.save(commit=False)
            impression.shampoo = shampoo
            impression.save()
            return redirect('cms:impression_list', shampoo_id=shampoo_id)
    else:
        form = ImpressionForm(instance=impression)

    return render(request,
                    'cms/impression_edit.html',
                    dict(form=form, shampoo_id=shampoo_id, impression_id=impression_id))


def impression_del(request, shampoo_id, impression_id):
    """感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', shampoo_id=shampoo_id)

