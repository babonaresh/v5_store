from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
<<<<<<< HEAD
from coupons.forms import CouponApplyForm
=======
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 size=cd['size'],
                 color=cd['color'],
                 update_size=cd['update'],
                 update_color=cd['update'],
                update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
<<<<<<< HEAD
        item['update_quantity_form'] = CartAddProductForm(
                            initial={'quantity': item['quantity'],
                            'size': item['size'],'color':item['color'],
                            'update': True})

    coupon_apply_form = CouponApplyForm()

    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form' : coupon_apply_form})
=======
            item['update_quantity_form'] = CartAddProductForm(
                              initial={'quantity': item['quantity'],
                              'size': item['size'],'color':item['color'],
                              'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db
