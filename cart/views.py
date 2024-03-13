from django.shortcuts import render, get_object_or_404
from .cart import Cart
from item.models import Item
from django.http import JsonResponse


def cart_summary(request):
    return render(request, 'cart.html', {})


def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('item_id'))
        item = get_object_or_404(Item, id=item_id)
        cart.add(item=item)

        cart_quantity = cart.__len__()

        response = JsonResponse({'Quantity': cart_quantity})
        return response


def delete(request):
    pass


def update(request):
    pass
