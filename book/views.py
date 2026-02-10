from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            description=request.POST.get('description')
        )
        return redirect('book_list')
    return render(request, 'books/book_form.html')


def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})


def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')
