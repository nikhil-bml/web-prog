from django.shortcuts import HttpResponseRedirect,render
from django.views import View
from .models import Product
from .forms import ProductSearchForm, QueryForm, RegisterForm, LoginForm
from .extras import full_text_search
from django.contrib.auth import authenticate,login,logout

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

class Search(View):
    template_name = "healthy_hunger/search.html"

    def get(self, request, product):
        context = {
            "products":full_text_search(factor=["name","ingredients"],model="Product", search_term=product)
        }
        return render(request, self.template_name ,context)
    
    def post(self, request, product):
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"/search/{request.POST.get('name')}/")
        return HttpResponseRedirect("/")

class Register(View):
    template_name = "healthy_hunger/register.html"
    form = RegisterForm
    def get(self, request):
        context = {"form":self.form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect("/register/")
        form.save()
        return HttpResponseRedirect("/login/")
        
class Login(View):
    template_name = "healthy_hunger/login.html"
    form = LoginForm
    def get(self, request):
        context = {"form":self.form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        user=authenticate(username=form.data["username"],password=form.data["password"])
        print(user)
        if not user:
            return HttpResponseRedirect("/login/")
        
        login(request, user)
        return HttpResponseRedirect("/")

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect("/login/")
        
