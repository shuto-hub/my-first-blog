from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout, login as django_login
from django.contrib.auth.models import User
from . import forms

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    user = request.user
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    comments = Comment.objects.filter(post=post)
    if request.method == "POST": #入力フォームはPOSTなので
        form = forms.CommentForm(request.POST)
        if form.is_valid(): #もし、formの内容が正しい時は
            comment = form.save(commit=False) #formの内容はまだセーブしません！
            comment.author = request.user
            comment.post = post
            comment.published_date = timezone.now()
            comment.save() #ユーザーを追加したのちにセーブ
    else:
        form = forms.CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post,'form': form,'comments': comments})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def mypage(request):
    posts = Post.objects.filter(author=request.user).order_by('published_date')
    user = request.user
    return render(request, 'blog/mypage.html',{'posts': posts}, {'user': user})