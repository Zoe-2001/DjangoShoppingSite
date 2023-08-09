from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone,formats

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.contrib.auth.models import User

from store.forms import LoginForm, RegisterForm
from store.models import Product, CartItem

from django.views.decorators.csrf import ensure_csrf_cookie

import json


def login_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'store/login.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = LoginForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'store/login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    return redirect(reverse('mainpage'))


def logout_action(request):
    logout(request)
    return redirect(reverse('login'))


def register_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, 'store/register.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = RegisterForm(request.POST)
    context['form'] = form

    # Validates the form.f
    if not form.is_valid():
        return render(request, 'store/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    new_item = Product(name = "men's clothes", category = "Yoga", gender = "Men",
                       image = "/static/images/mencloth.jpg", price = "10.99")
    new_item.save()

    login(request, new_user)
    return redirect(reverse('mainpage'))



def login_check(request):
    if not request.user.is_authenticated or not request.user or not request.user.id or not request.user.email.endswith(""):
        return False
    return True

def _my_json_error_response(message, status=200):
    response_json = '{ "error": "' + message + '" }'
    return HttpResponse(response_json, content_type='application/json', status=status)


@login_required
@ensure_csrf_cookie
def mainpage_action(request):
    if not login_check(request):
        return _my_json_error_response("You must be logged in to do this operation", status=401)

    products = Product.objects.all()
    # Just display global page form if this is a GET request.
    if request.method == 'GET':
        return render(request, 'store/mainpage.html', {'products': products})

    return render(request, 'store/mainpage.html', {'products': products})

@login_required
def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})



@login_required
def add_to_cart(request):
    user = request.user
    product_id = int(request.POST['product_id'])

    try:
        cart_item = CartItem.objects.get(user=user, product_id=product_id)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem(user=user, product=product, quantity=1)
        cart_item.save()


    return JsonResponse({'message': 'Product added to cart.'})