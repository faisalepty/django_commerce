from django.shortcuts import render, redirect
from .models import *
from .forms import QuantityForm

from django.contrib import messages


from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .models import *


# Create your views here.

@login_required(login_url='login')
def Home(request):
    context = {}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def Productsd(request):
    products = Products.objects.all()
    message = request.session.pop('message', None)
    context = {'products': products, 'message':message}
    return render(request, 'base/products.html', context)

@login_required(login_url='login')
def About(request):
    return render(request, 'base/about.html')

def UserRegistration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.info(request, 'An error occured while trying to handle your form')
            
    context = {'form': form}
    return render(request, 'base/register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'base/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def CartPage(request, pk, pk2=None):
    oders = Oder.objects.filter(user_id=pk)
    form = QuantityForm()
    previouse = request.META.get('HTTP_REFERER')
    total = 0
    for oder in oders:
        total += oder.products.price * oder.quantity
    if pk2:
        if request.method == 'POST':
            oder = Oder.objects.get(user_id=pk, products_id=pk2)
            form = QuantityForm(request.POST, instance=oder)
            if form.is_valid():   
                form.save()
                return redirect(previouse)
    context = {'orders':oders,'form':form, 'total':total}
    return render(request, 'base/cart.html', context)

@login_required(login_url='login')
def AddToCart(request, pk, pk2):
    odercount = Oder.objects.filter(user_id=pk).count()
    try:
       oder = Oder.objects.get(user_id=pk, products_id=pk2)
       request.session['message'] = 'Item already in cart'
    except:
        oder = Oder.objects.create(user_id=pk, products_id=pk2)
        return redirect('products')
    return redirect('products')

@login_required(login_url='login')
def DelCart(request, pk):
    previous_page = request.META.get('HTTP_REFERER')
    oder = Oder.objects.get(id=pk)
    oder.delete()
    messages.success(request, 'item deleted')
    return redirect(previous_page)