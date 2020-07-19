from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Author
from .forms import BlogForm, AuthorForm

def index(request):
    context = {'title': 'Home'}
    return render(request, 'homepage/index.html', context)

def blogs(request):
    data = Blogs.objects.all()
    context = {
        'title': 'Blogs',
        'data': data
    }
    return render(request, 'homepage/blogs.html', context)

def blog_detail(request, blog_id):
    data = Blogs.objects.get(id=blog_id)
    return render(request, 'homepage/blog_detail.html', context={
        'title': 'Blogs | ' + data.blog_title,
        'data':data
    })

def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/blogs')
        else:
            print("Form is invalid")
    else:
        form = BlogForm()
    return render(request, 'homepage/blog_create.html', {
        'title': 'New Blog',
        'form': form
    })

def blog_update(request, blog_id):
    obj = get_object_or_404(Blogs, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=obj)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/blogs')
        else:
            print("Form is invalid")
    else:
        form = BlogForm(instance=obj)
    return render(request, 'homepage/blog_create.html', {
        'title': 'Edit Blog',
        'form': form
    })

def blog_delete(request, blog_id):
    blog_object = get_object_or_404(Blogs, id=blog_id)
    blog_object.delete()
    return redirect('/blogs')

def authors(request):
    data = Author.objects.all()
    context = {
        'title': 'Authors',
        'data': data
    }
    return render(request, 'homepage/authors.html', context)

def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/authors')
        else:
            print("Form is invalid")
    else:
        form = AuthorForm()
    return render(request, 'homepage/author_create.html', {
        'title': 'Edit Author',
        'form': form
    })

def author_update(request, author_id):
    obj = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=obj)
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid")
            form.save()
            return redirect('/authors')
        else:
            print("Form is invalid")
    else:
        form = AuthorForm(instance=obj)
    return render(request, 'homepage/author_create.html', {
        'title': 'Edit Author',
        'form': form
    })

def author_delete(request, author_id):
    author_object = get_object_or_404(Blogs, id=author_id)
    author_object.delete()
    return redirect('/authors')