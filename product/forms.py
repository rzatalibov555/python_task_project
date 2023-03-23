from django import forms
from .models import Product


# class ProductForm(forms.Form):
#     name = forms.CharField()
#     surname = forms.CharField()

class ProductForm(forms.ModelForm):
    # -----------------------------------WIDGETS-- method 2 -----------------------------
    # description = forms.CharField(widget=forms.Textarea(attrs={"cols": 23, "rows": 5}))

    class Meta:
        model = Product
        # variant 1 (lazim olan fieldleri cagirmaq ucun adlarini yazmaq lazimdir)
        # fields = ("name", "price", "author")

        # variant 2 ("__all__" -string-de all yazmaqla hamisini cagira bilerik)
        # fields = "__all__"

        # variant 3 (exclude istifdade ederek icine lazim olmayan fieldlerin adlarini yazmaqla, diger lazim olanlari cagira bilerik.)
        # exclude = ["tags","price"]
        exclude = ("tags",)
        # -----------------------------------WIDGETS- method 1------------------------------
        # widgets = {
        #     "description": forms.Textarea(attrs={"cols": 23, "rows": 5, "class": "form-control border"})
        # }

        # https: // docs.djangoproject.com / en / 4.1 / topics / forms / modelforms /  # modelform


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['description'].widget.attrs.update({"class":"form-control"})
        # self.fields['description'].widget.attrs["class"] = "form-control border"

        for field in self.fields:
            # print(field)
            self.fields[field].widget.attrs.update({"class":"form-control border"})




    def clean(self):
        attrs = self.cleaned_data
        # print(attrs)
        # return attrs
        name            = attrs.get("name")
        price           = attrs.get("price")
        tax_price       = attrs.get("tax_price", None)
        discount_price  = attrs.get("discount_price", None)

        total_price = price + (tax_price or 0) - (discount_price or 0)

        if total_price < 0:
            raise forms.ValidationError("<b>Umumi mebleg 0-dan kicik</b> ola bilmez!")

        if name.startswith("a"):
            raise forms.ValidationError("Name balaca a ile baslaya bilmez!")
        return attrs



    def save(self, commit=True):
        if commit:
            print("We are inside save. Here you can send mail to")
            return Product.objects.create(
                **self.cleaned_data
            )
        # else:
            # return Product(**self,cleaned_data)
#TODO:: neyese gore formdaki 71-ci setrdeki else iwlemedi (def save())