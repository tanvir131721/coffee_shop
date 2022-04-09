
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from .models import Our_brunches, contact
from django.contrib import messages

# Create your views here.

def index(request):
    state = Our_brunches.objects.all()
    context={
            "state":state
    }
    if request.method == 'POST':
            index = contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            index.name=name
            index.email=email
            index.phone=phone
            index.message=message
            index.save()
            return HttpResponse("<h1>Thanks for contacting with us. Wait for our reply!</h1>")
            
    return render(request, 'index.html',context)


def show_data(request) :
        data=contact.objects.all()
        return render(request,'show_data.html',{"contact":data})