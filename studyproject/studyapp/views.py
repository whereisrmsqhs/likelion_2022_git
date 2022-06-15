from django.shortcuts import redirect, render, get_object_or_404
from .models import Community
from .forms import CommuForm, Community, CommentForm

def home(request):
    posts = Community.objects.all()
    return render(request, 'home.html', {'posts':posts})

def modelform(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = CommuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommuForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Community, pk=post_id)

    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Community, pk=post_id)
        finished_form.save()

    return redirect('detail', post_id)