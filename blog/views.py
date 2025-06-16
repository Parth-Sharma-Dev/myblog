from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'post.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')