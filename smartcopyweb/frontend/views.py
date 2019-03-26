from django.shortcuts import render
from django.http import JsonResponse

import nltk


def smart_copy_en(request):
    if request.method == 'GET':
        return render(request, 'smartcopy.html', locals())

    if request.method == 'POST':
        text_input = request.POST.get('textinput', False)

        if text_input:
            text_output = sentence_split_by_br(text_input)

        return render(request, 'smartcopy.html', locals())


def sentence_split_by_br(text):
    text_output = ""
    sents = nltk.sent_tokenize(text)
    for _s in sents:
        s = ' '.join(_s.split(), )
        print(s)
        text_output += s + "&#13;&#10" + "&#13;&#10"

    print(text_output)
    return text_output

