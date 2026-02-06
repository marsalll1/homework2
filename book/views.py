from django.shortcuts import render
from django.http import HttpResponse
def review_book(request):
    if request.method == 'GET':
        return HttpResponse('Счастье можно найти даже в тёмные времена, если не забывать обращаться к свету')
