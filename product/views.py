from django.shortcuts import render
from .models import Product
# Create your views here.


def product_list_view(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "product/list.html", context=context)
