from django.shortcuts import render,redirect
from food.models import Food
from django.contrib.auth.models import User as user

def home(request):
    return render(request, 'food/home.html')
    
def about(request):
    return render(request, 'food/about.html')

def offer(request):
    if request.method=='POST':
        title = request.POST['title']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        date = request.POST['date']
        time = request.POST['time']
        quantity = request.POST['quantity']
        comment = request.POST['comment']
        status = request.POST['status']
        author = request.user
        ins = Food(title=title, fname=fname, lname=lname, phone_number=phone_number, address=address, date=date, time=time, quantity=quantity, comment=comment, status=status, author=author)
        ins.save()  
        return redirect('food_offered')
    return render(request, 'food/offer.html')
    
def food_offered(request):
    return render(request, 'food/food_offered.html')

def status(request):
    orders = Food.objects.all()
    food_orders = orders.filter(author = request.user)
    return render(request, 'food/status.html', {'food_orders':food_orders})


      