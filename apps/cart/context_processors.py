from django.shortcuts import render

from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
