from django.shortcuts import HttpResponseRedirect,render
from django.views import View
from .models import Product

class Home(View):
    template_name = "healthy_hunger/home.html"
    def get(self, request):
        context = {
            "products":[]
        }
        popular_items = [1,2,3,4]
        [context["products"].append(Product.objects.get(pk=pk)) for pk in popular_items if Product.objects.filter(pk=pk).exists()]

        return render(request, self.template_name, context)

class ProductView(View):
    template_name = "healthy_hunger/product.html"
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if not Product.objects.filter(pk=pk):
            return HttpResponseRedirect("/")
        
        context={
            "product": product
        }

        return render(request, self.template_name, context)
