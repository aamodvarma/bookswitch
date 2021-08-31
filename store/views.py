from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
import datetime
from django.views.generic import ListView, DetailView
from django.contrib import messages


# Create your views here.
@csrf_exempt
def store(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'store/store.html', context)

@csrf_exempt
def fiction(request):
    products = Product.objects.filter(category='fiction')
    context = {'products': products}
    return render(request, 'store/fiction.html', context)

@csrf_exempt
def fiction_slider(request):
    products = Product.objects.filter(category='fiction')
    context = {'products': products}
    return render(request, 'store/fiction_slider.html', context)

@csrf_exempt
def academic(request):
    products = Product.objects.filter(category='academic')
    context = {'products': products}
    return render(request, 'store/academic.html', context)



@csrf_exempt
def academic_slider(request):
    products = Product.objects.filter(category='academic')
    context = {'products': products}
    return render(request, 'store/academic_slider.html', context)

@csrf_exempt
def productdetails(request, uploadid):
    product = Product.objects.get(uploadid=uploadid)
    return render(request, 'store/product.html', {'product': product})

@csrf_exempt
def shipping(request):
    if  request.user.is_authenticated:

        shipping = ShippingAddress()
        valid = ShippingAddress.objects.filter(customer=request.user.profile)
        if valid:
            return redirect('store')
        else:
            if request.method == "POST":
                shipping.customer = request.user.profile
                shipping.address = request.POST.get('address')
                shipping.city = request.POST.get('city')
                shipping.zipcode = request.POST.get('zipcode')
                shipping.save()
                return redirect('store')
            return render(request, 'store/shipping.html')
    else:
        return redirect('login')


@csrf_exempt
def give(request):
    if request.method == "POST":
        book = Product()
        book.owner = request.user.profile
        book.bookname = request.POST.get('bookname')
        book.category = request.POST.get('category')
        book.price = request.POST.get('price')
        book.uploadid = str(datetime.datetime.now())[0:-7].replace(' ', '').replace('-', '').replace(':', '')
        if len(request.FILES) != 0:
            book.image = request.FILES['image']
        book.save()
        return redirect('dashboard')

    return render(request, 'store/give.html')


def home(request):
    context = {}
    return render(request, 'store/store.html', context)

@csrf_exempt
def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username OR Password is incorrect")
                print()
        context = {}
        return render(request, 'store/login.html')

    else:
        products = Product.objects.filter(owner__user=request.user)
        context = {'products': products}
        return render(request, 'store/dashboard.html', context)


@csrf_exempt
def logoutuser(request):
    logout(request)
    return redirect('loginpage')

@csrf_exempt
def register(request):
    if not request.user.is_authenticated:
        #    user_form = ProfileForm(request.POST)
        #    if request.method == "POST":
        #        if user_form.is_valid():
        #            user_form.save()
        #            messages.success(request, "Account was Create for " + user_form.cleaned_data.get('username'))
        #
        #            return redirect('loginpage')
        #
        #    context = {'form': user_form}
        #    return render(request, 'store/register.html', context)
        if request.method == 'POST':

            form = UserForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                profile = Profile()
                profile.user = user
                profile.email = user.email
                profile.phone_number = request.POST.get('phonenumber')
                profile.save()
                messages.success(request, ('Your profile was successfully updated!'))
                return redirect('dashboard')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            form = UserForm()
        return render(request, 'store/register.html', {'form': form, })

    else:
        products = Product.objects.filter(owner__user=request.user)
        context = {'products': products}
        return render(request, 'store/dashboard.html', context)

@csrf_exempt
def delete_book(request, uploadid):
    product = Product.objects.filter(uploadid=uploadid)[0]
    if str(product) == str(request.user):
        product.delete()
    else:
        messages.error(request, ('You do not have to authentication to perform that action'))
    return redirect('dashboard')

@csrf_exempt
def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(owner__user=request.user)
        context = {'products': products}
        return render(request, 'store/dashboard.html', context)
    else:
        items = []
        context = {}
        return redirect ('loginpage')

