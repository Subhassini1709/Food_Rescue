from django.contrib.auth.backends import UserModel
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import volunteer
from django.contrib.auth.models import User

def registerPage(request):
    if request.user.is_authenticated:
        if UserModel.is_superuser or UserModel.is_staff:
            return redirect('/admin/')
        else :
            return redirect('Dashboard')
    else :
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form}) 

def loginPage(request):
    if request.user.is_authenticated:
        # if UserModel.is_superuser or UserModel.is_staff:
        #    return redirect('/admin/')
        #else :
        return redirect('Dashboard')
        
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return redirect('/admin/')
                else :
                    login(request, user)
                    return redirect('Dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'food/dashboard.html')


def logoutPage(request):
    logout(request)
    return render('logout')


def volunteerPage(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        status = request.POST['status']
        ins = volunteer(name=name, phone_number=phone_number,
                        email=email, address=address, status=status)
        ins.save()
        return redirect('thanks')
    return render(request, 'users/volunteer.html')


def thanksvolunteerPage(request):
    return render(request, 'users/thanks_volunteer.html')

def dashboard(request):
    use = User.objects.all()
    users = use.filter(username = request.user.username)
    return render(request, 'food/dashboard.html', {'users':users})
