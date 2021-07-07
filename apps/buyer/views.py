
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Buyer


# Create your views here.
from ..order.models import OrderItem, Order


def become_buyer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            buyer = Buyer.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'buyer/become_buyer.html', {'form': form})


def profile(request):
    context = {}
    ch = User.objects.filter(username=request.user.username)
    data = User.objects.get(username=request.user.username)
    context["data"] = data

    all_orders = []
    orders = OrderItem.objects.filter(ch)
    for order in orders:
        products = []
        ord = {
            "order": order,
            "products": products,
        }
        all_orders.append(ord)
    context["order_history"] = all_orders
    return render(request, 'buyer/buyer_profile.html', context)
