from django.shortcuts import render, redirect
from django.contrib import messages

from myuser.models import myuser

from django.core.paginator import Paginator
# Create your views here.


def mainpage(request):

    user1 = myuser.objects.all().order_by('score').reverse()[:1]
    user2 = myuser.objects.all().order_by('score').reverse()[1:2]
    user3 = myuser.objects.all().order_by('score').reverse()[2:3]

    context = {
        'user1': user1,
        'user2': user2,
        'user3': user3,
    }

    return render(request, 'pages/mainpage.html', context)



def search(request):

    if(request.method == 'POST'):
        
        username = request.POST['username']

        user_list = myuser.objects.filter(username = username)

        users_list = myuser.objects.all().order_by('score').reverse()
        paginator = Paginator(users_list, 4) # Show 20 user per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context= {
            'users': page_obj,
            'user': user_list,
        }

        return render(request, 'pages/ranks.html', context)

    else:
        user_list = None
        users_list = myuser.objects.all().order_by('score').reverse()
        paginator = Paginator(users_list, 4) # Show 20 user per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context= {
            'users': page_obj,
            'user': user_list,
        }
        return render(request, 'pages/ranks.html', context)

