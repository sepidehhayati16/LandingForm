from django.shortcuts import render , redirect
from . import models
from django.contrib import messages

# Create your views here.
def landing(request):
    return render(request, 'index.html')
def sendMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        instance = models.message.objects.create(name=name, email=email, phone=phone, message=message)
        instance.save()
        messages.success(request, f'Your message has been sent successfully!')
        return redirect('landing')
    else:
        messages.success(request,'Your message was not sent successfully')
        return redirect(request, 'landing')