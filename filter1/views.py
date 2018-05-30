from typing import List, Any

from boto.gs import user
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from .models import Data, Subcat, Subsubcat

'''
def selectview(request):
    item = Data.objects.all()  # use filter() when you have sth to filter ;)
    form = request.POST
    if request.method == 'POST':
        selected_item = get_object_or_404(Data, pk=request.POST.get('cat_id'))
        # get the user you want (connect for example) in the var "user"
        user.item = selected_item
        user.save()

        # Then, do a redirect for example
        print(item)

    return render(request, 'filter1/f1.html', {'items': item}, )

def home(request):
    if request.method == 'POST':
        form = Sort(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print(user.value)
            return render(request, 'filter1/index.html',)
    else:
        form = Sort()
    return render(request, '.html', {'form': form})
'''


# Create your views here.
def index_view(request):
    # item = Data.objects.distinct('cat_id')  # use filter() when you have sth to filter ;)
    item = Data.objects.values_list('cat_id').distinct()
    print(item)
    form = request.POST
    if request.method == 'POST':
        selected_item = get_object_or_404(Data, pk=request.POST.get('cat_id'))
        # get the user you want (connect for example) in the var "user"
        user.item = selected_item
        user.save()

        # Then, do a redirect for example

    return render(request, 'filter1/index.html', {
        'items': item,
        'query_results': Data.objects.all(),
    })


def category(request):
    form = request.POST
    if request.method == 'POST':
        print(form)
        # user_value = form.Category
        uv = form["Category"][2]
        print(uv)
        a = "('1',)"
        if int(uv) is 1:
            return f1(request, int(uv))
        elif int(uv) is 2:
            return f1(request, int(uv))
        else:
            return render(request, 'filter1/ok.html')
    else:
        return render(request, 'filter1/ok.html')


def f1(request,uv):

    a = Data.objects.filter(cat_id=uv).all()
    result: List[Any] = []
    for i in a:
        result.append(i.subcat_set.all())

    if uv is 1:
        return render(request, 'filter1/f1.html', {
            'query_results': a,
            'cate': result,
        })
    elif uv is 2:
        return render(request, 'filter1/f2.html', {
            'query_results': a,
            'cate': result,
        })

    else:
        return render(request, 'filter1/ok.html')

def f2(request):
    a = Data.objects.filter(cat_id=2).all()
    result: List[Any] = []
    for i in a:
        result.append(i.subcat_set.all())

    return render(request, 'filter1/f2.html', {
        'query_results': a,
        'cate': result,
    })


def fs21(request):
    a = Data.objects.filter(cat_id=2).all()
    result = []
    rt = []
    for i in a:
        result.append(i.subcat_set.all())

    for i in result:
        rt.append(Subcat.objects.filter(c_id=21).all())

    return render(request, 'filter1/f2.html', {
        'query_results': a,
        'cate': result,
        'subcate': rt,
    })
