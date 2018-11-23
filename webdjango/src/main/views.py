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
        result = obj.search(keyword, sum_op = 'text', SENTENCES_COUNT=2)
        paginator = Paginator(result, 10)
        get_page = request.GET.get('page')
        result = paginator.get_page(get_page)
    except Exception as e:
        print(e)
        result = None
    context = {'keyword': keyword, 'result' : result, 'page' : page}
    template = 'search.html'

    return render(request, template, context)
