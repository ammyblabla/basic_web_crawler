from django.shortcuts import render, redirect
from myelasticsearch.search import searcher

def index(request):
    keyword = request.GET.get('q-samsung')
    if keyword == None:
        context = {'keyword': keyword}
        template = 'index.html'
    else:
        return redirect('search', keyword)
    
    return render(request, template, context)

def search(request, keyword=None, page=1, obj=searcher()):
    keyword = request.GET.get('q-samsung')
    if keyword == None:
        return redirect('index')
    try:
        result = obj.search(keyword, sum_op = 'url', SENTENCES_COUNT=2)
    except:
        result = None
    context = {'keyword': keyword, 'result' : result, 'page' : page}
    template = 'search.html'

    return render(request, template, context)
