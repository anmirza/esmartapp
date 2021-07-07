from django.shortcuts import render
from apps.products.models import Product


# Create your views here.
def frontpage(request):
    newest_product = Product.objects.all()
    return render(request, 'core/frontpage.html', {'newest_product': newest_product})


def contact(request):
    return render(request, 'core/contact.html')


def about_us(request):
    return render(request, 'core/about.html')


def signupas(request):
    return render(request, 'core/signupas.html')
