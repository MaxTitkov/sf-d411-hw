from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from p_library.models import Book, Redaction
from django.template import loader



def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку", 'books': books}
    return HttpResponse(template.render(biblio_data, request))

@csrf_exempt
def book_increment(request):
    if request.method == "POST":
        book_id = request.POST["id"]
        if not book_id:
            return redirect("/index/")
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect("/index/")
            book.copy_count += 1
            book.save()
        return redirect("/index/")
    else:
        return redirect("index/")

@csrf_exempt
def book_decrement(request):
    if request.method == "POST":
        book_id = request.POST["id"]
        if not book_id:
            return redirect("/index/")
        else:
            book = Book.objects.filter(id = book_id).first()
            if not book:
                return redirect("/index/")
            if book.copy_count < 0:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect("/index/")
    else:
        return redirect("/index/")

def redaction(request):
    template = loader.get_template("redactions.html")
    books = Book.objects.all()
    redactions = Redaction.objects.all()
    books_data = {"books": books, "redactions": redactions}
    return HttpResponse(template.render(books_data))

