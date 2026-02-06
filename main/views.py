from django.http import HttpResponse

def index(request):
    return HttpResponse('Счастье можно найти даже в тёмные времена, если не забывать обращаться к свету')
