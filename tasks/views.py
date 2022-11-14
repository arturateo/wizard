from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone
from .models import Post
# from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'tasks/tasks_list.html', {'posts': posts})

def tasks_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'tasks/tasks_detail.html', {'post': post})
