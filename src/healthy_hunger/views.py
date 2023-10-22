from django.shortcuts import HttpResponseRedirect,render
from django.views import View
from .models import Product

class Home(View):
    template_name = "healthy_hunger/home.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

class ProductView(View):
    template_name = "healthy_hunger/product.html"
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if not Product.objects.filter(pk=pk):
            return HttpResponseRedirect("/")
        
        context={
            "product_image":product.product_image.url,
            "nutrition_image":product.nutrition_image.url,
            "description":product.description,
            "name":product.name,
            "ingredients":product.ingredients
        }
        return render(request, self.template_name, context)
