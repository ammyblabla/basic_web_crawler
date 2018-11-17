from django.shortcuts import render, redirect
from myelasticsearch.search import searcher
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    paginator = Paginator(result, 2)
    get_page = request.GET.get('page')
    result = paginator.get_page(get_page)
    context = {'keyword': keyword, 'result' : result, 'page' : page}
    template = 'search.html'

    return render(request, template, context)
