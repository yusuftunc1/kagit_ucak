from django.shortcuts import render, redirect
from django.contrib import messages

from myuser.models import myuser

from django.core.paginator import Paginator

# Create your views here.


def register(request):
    if (request.method == 'POST'):
        
        #form değerlerini alma
        username = request.POST['username']
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']

        #username kontrol
        if myuser.objects.filter(username = username).exists():
            messages.add_message(request, messages.WARNING, "Bu kullanıcı adı daha önce alınmış" )

            return redirect('register')
        else:
            #mail kontrol
            if myuser.objects.filter(email = email).exists():
                
                messages.add_message(request, messages.WARNING, "Bu mail daha önce alınmış")
                return redirect('register')
            else:
                #okey create user
                user = myuser.objects.create(username= username, firstname= name, lastname= lastname, email= email, phonenum = phone)
                user.save()
            
                messages.add_message(request, messages.SUCCESS, 'Kullanıcı oluşturuldu')
                return redirect('mainpage')
    else:
        return render(request, 'user/register.html')




