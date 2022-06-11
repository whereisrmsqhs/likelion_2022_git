from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, Comment

def home(request):
    #블로그 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    posts = Blog.objects.filter().ordered_by('-date')
    return render(request, 'index.html', {'posts':posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# GET/POST 요청 둘 다 처리가 가능
def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서 detail.html로 띄어주는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    
    return redirect('detail', blog_id)