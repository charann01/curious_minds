from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from .models import Books
# Create your views here.
#create the book
def CreateBook(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print('book created')
        else:
            print('form is not valid')
    return render(request,'books/create.html',{"form":form})


# listing all the books
def ListBooks(request):
    context = {}
    context['books'] = Books.objects.all().order_by('bookname')
    return render(request,'books/list.html',context)


# gettting the detail of a particular book
def DetailView(request,pk):
    context = {}
    try:
        book = Books.objects.get(id=pk)
        context['book'] = book
    except:
        context['book'] = "empty, no such book"
        print("book doesn't exist")
    return render(request,'books/details.html',context)


# deleting a book
def DeleteView(request,pk):
    context = {}
    try:
        Books.objects.get(id=pk).delete()
        return HttpResponse('The book has been deleted')
    except:
        context['book'] = "empty, no such book"
        return HttpResponse('unable to delete')

def UpdateView(request,pk):
    context = {}
    if request.method == "POST":
        price = request.POST['price']
        description = request.POST['description']
        try:
            book = Books.objects.get(id=pk)
            book.price = price
            book.description = description
            book.save()
            return HttpResponse('Book Updated')
        except:
            context['book'] = "No such Book"
            return HttpResponse('No book')
    return render(request,'books/update.html',context)

def SearchView(request):
    context = {}
    if request.method == "POST":
        name = request.POST['book name']
        books = Books.objects.filter(bookname=name)
        context['books'] = books
        return render(request,'books/search.html',context)
    return render(request,'books/search.html',{})

def HomeView(request):
    return render(request,'home.html',{})
