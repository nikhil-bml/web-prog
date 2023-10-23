from django.shortcuts import HttpResponseRedirect,render
from django.views import View
from .models import Product
from .forms import ProductSearchForm, QueryForm
class Home(View):
    template_name = "healthy_hunger/home.html"
    form = ProductSearchForm
    def get(self, request):
        context = {
            "products":[],
            "form":self.form
        }
        popular_items = [1,2,3,4]
        [context["products"].append(Product.objects.get(pk=pk)) for pk in popular_items if Product.objects.filter(pk=pk).exists()]

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/search/{request.POST.get('name')}")
        return HttpResponseRedirect("/")
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
class AboutView(View):
    template_name = "healthy_hunger/about.html"
    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)
    
class TermsView(View):
    template_name = "healthy_hunger/terms_cond.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

class ContactView(View):
    template_name = "healthy_hunger/contact.html"
    form = QueryForm
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/contact')