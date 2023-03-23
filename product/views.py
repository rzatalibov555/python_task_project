
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
from .forms import ProductForm
# Create your views here.



# region important

# todo: EDILMELI OLAN TOTDO LIST
# todo: region important ve endregin lazim olar regionlari acib baglamaq ucundur.

# endregion

def product_list_view(request):

    # print(request.method)

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
    return render(request, "product/detail.html" ,context)




def product_create_view(request):
    context = {}
    form = ProductForm()


    if request.method == "POST":
        print(request.POST)
        form = ProductForm(data = request.POST)

        # inputlarin deyerlerinin basqa formada cagirilmasi
        # name = request.POST.get("name")
        # print(name)

        if form.is_valid():
            # form.save()
            product = form.save(commit=True)
            print(product)
            # product.price = 10
            # product.save()
            return redirect("product:list")
        else:
            print(form.errors)

    context["form"] = form
    return render(request, "product/create.html", context)