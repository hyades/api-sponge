from django.http import JsonResponse


def test_get(request):
    resp = {}
    resp['http_method'] = request.method
    resp['params'] = dict(request.GET)
    resp['path'] = request.path
    resp['body'] = request.body
    resp['headers'] = {}
    resp['headers']['CONTENT_LENGTH'] = request.META['CONTENT_LENGTH']
    resp['headers']['CONTENT_TYPE'] = request.META['CONTENT_TYPE']
    resp['headers']['HTTP_ACCEPT'] = request.META['HTTP_ACCEPT']
    resp['headers']['HTTP_ACCEPT_ENCODING'] = request.META[
        'HTTP_ACCEPT_ENCODING']
    resp['headers']['HTTP_HOST'] = request.META['HTTP_HOST']
    resp['headers']['QUERY_STRING'] = request.META['QUERY_STRING']
    resp['headers']['HTTP_USER_AGENT'] = request.META['HTTP_USER_AGENT']
    return JsonResponse(resp)


def test_post(request):
    resp = {}
    resp['http_method'] = request.method
    resp['params'] = dict(request.REQUEST)
    resp['path'] = request.path
    resp['body'] = request.body
    resp['headers'] = {}
    resp['headers']['CONTENT_LENGTH'] = request.META['CONTENT_LENGTH']
    resp['headers']['CONTENT_TYPE'] = request.META['CONTENT_TYPE']
    resp['headers']['HTTP_ACCEPT'] = request.META['HTTP_ACCEPT']
    resp['headers']['HTTP_ACCEPT_ENCODING'] = request.META[
        'HTTP_ACCEPT_ENCODING']
    resp['headers']['HTTP_HOST'] = request.META['HTTP_HOST']
    resp['headers']['QUERY_STRING'] = request.META['QUERY_STRING']
    resp['headers']['HTTP_USER_AGENT'] = request.META['HTTP_USER_AGENT']

    return JsonResponse(resp)
