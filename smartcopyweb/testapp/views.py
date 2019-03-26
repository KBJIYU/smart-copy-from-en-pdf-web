from django.shortcuts import render
from django.http import JsonResponse

from .modules.testmodules import test_module


def test_api(request):
    msg = {'msg': 'ok'}

    return JsonResponse(msg)


def test_html(request):
    test_h1 = 'hi hunter'
    module_return = test_module()

    return render(request, 'testapp/testuse.html', locals())
