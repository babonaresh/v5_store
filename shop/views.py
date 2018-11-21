from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm
from .forms import *
<<<<<<< HEAD
from .models import Category, Product, ProductFilter
from cart.forms import CartAddProductForm
from .forms import  SearchForm
from haystack.query import SearchQuerySet
=======
from .models import Category, Product
from cart.forms import CartAddProductForm
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'shop/register_done.html', {'new_user': new_user})
    else:
      user_form = UserRegistrationForm()
      return render(request, 'shop/register.html', {'user_form': user_form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
<<<<<<< HEAD
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
=======
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
<<<<<<< HEAD
                   'products': products,'filter': filter})
=======
                   'products': products})
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
<<<<<<< HEAD

def product_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(product_list) \
                .filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
    return render(request,
                  'shop/product/search.html',
                  {'form': form,
                   'cd': cd,
                   'results': results,
                   'total_results': total_results})
=======
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db
