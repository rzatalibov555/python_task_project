from django.shortcuts import render, get_object_or_404
from .models import Product

from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
# Create your views here.


def product_list_view(request):
    context = {

        "products" : Product.objects.all(),

        # variant1 (# get total price)

        # "products": Product.objects.annotate(
        #     tax      = Coalesce(F("tax_price"), 0, output_field=FloatField()),
        #     discount = Coalesce(F("discount_price"), 0, output_field=FloatField()),
        # ).annotate(
        #     total_price = F("price")+F("tax")-F("discount")
        # ).all()


        # varaint 2 - models -> total_price functionunda (# get total price)
    }

    return render(request, "product/list.html", context=context)



def product_detail_view(request, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    context = {
        "product" : product
    }
    return render(request, "product/detail.html",context)