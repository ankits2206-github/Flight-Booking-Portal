from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')


    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):

    if request.method == 'POST':
        f_name=request.POST["firstname"]
        l_name=request.POST["lastname"]
        u_name=request.POST["username"]
        email=request.POST["email"]
        p1=request.POST["password1"]
        p2=request.POST["password2"]

        if(p1==p2):

            if (User.objects.filter(username=u_name).exists() == True):
                messages.info(request,'Username already taken')
                return redirect('/registration/register')
            elif(User.objects.filter(email=email).exists()==True):
                messages.info(request,'email already taken')
                return redirect('/registration/register')
            else:
                user=User.objects.create_user(username=u_name,password=p1,first_name=f_name,last_name=l_name,email=email)
                user.save()
                nm = f_name+l_name
                subject = 'welcome to All Flight world'
                message = f'Hi {nm}({u_name}), thank you for registering in AllFlight.com. Hope you will enjoy our feature. Thanks..'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail(subject, message, email_from, recipient_list)

                messages.info(request,'Account created')
                return redirect('login')

        else:
            messages.info(request,'Password not matched')
            return redirect("/registration/register")

    else:
        return render(request,'register.html')
