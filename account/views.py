from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User


def login_view(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = AuthenticationForm(request=req,data=req.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(req,username=username,password=password)

                if user is not None:
                    login(req,user=user)
                    return redirect('/')
                
            else:
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                u = User.objects.get(email=email)

                user = authenticate(req,username=u.username,password=password)
                    
                if user is not None:
                    login(req,user=user)
                    return redirect('/')
                
            
                
                
        form = AuthenticationForm()
        ctx = {'form' : form}
        return render(req,'accounts/login.html',ctx)
    else:
        return redirect('/')

@login_required
def logout_view(req):
    logout(req)
    return redirect('/')


def signup_view(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = UserCreationForm(req.POST)
            if form.is_valid():
                form.save()
                user = User.objects.get(username=req.POST['username'])
                user.email = req.POST['email']
                user.save()
                return redirect('/')

        form = UserCreationForm()
        ctx = {'form' : form}
        return render(req,'accounts/signup.html',ctx)
    else:
        return redirect('/')


def reset_view(req,**kwargs):
    if not req.user.is_authenticated:
        id = kwargs.get('uid')
        if req.method == "POST":
            data = req.POST
            user = User.objects.get(id=id)
            if user is not None:
                    if data['password'] == data['repassword']:
                        user.set_password(data['password'])
                        user.save()
                        return redirect('/account/login')
        ctx = {'id':id}
        return render(req,'accounts/reset.html',ctx)
    else:
        return redirect('/')


def forget_view(req):
    if req.method == 'POST':
        email = req.POST['email']
        user = User.objects.get(email=email)
        reset_link = f'http://127.0.0.1:8000/account/reset/{user.pk}'
        send_mail(
            'بازیابی رمز عبور',
            f'برای بازیابی رمز عبور خود از لینک زیر استفاده کنید: {reset_link}',
            'amirsly11@gmail.com',
            [email],
            fail_silently=False,
        )
        return redirect('/account/login')
    return render(req, 'accounts/forget.html')