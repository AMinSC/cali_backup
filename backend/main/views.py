from django.http import HttpResponse


from search_engine.meili_customize.config import Config
from search_engine.meili_customize.search import Search


def custom_search(request):
    s = request.GET.get('q', '')

    if not s:
        return HttpResponse('Not string..!')

    conf = Config()
    sch = Search(conf)
    result = sch.search(s)

    return HttpResponse(f'Answer: {result}')
