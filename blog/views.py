from django.shortcuts import render
from .models import Post, Contact
from datetime import datetime
from django.contrib import messages

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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message, date_time=datetime.today())
        contact.save()
        messages.success(request, ' Your message has been sent.')

    return render(request, 'contact.html')