from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    allusers = User.objects.all()
    context = {
        'allusers': allusers
    }
    return render(request,'index.html',context)


def addUser(request):
    try:
        tempfirst = request.POST['firstname']
        templast = request.POST['lastname']
        tempemail = request.POST['email']
        tempage = int(request.POST['age'])

        User.objects.create(first_name=tempfirst,last_name=templast,email_address=tempemail,age=tempage)
        return redirect('/')
    except:
        print('Invalid inputs - user not created')
        return redirect('/')

    # tempfirst = request.POST['firstname']
    # templast = request.POST['lastname']
    # tempemail = request.POST['email']
    # tempage = int(request.POST['age'])

    # User.objects.create(first_name=tempfirst,last_name=templast,email_address=tempemail,age=tempage)
    # print(User.objects.first())
    # return redirect('/')

