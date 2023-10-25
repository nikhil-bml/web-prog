from django.shortcuts import HttpResponseRedirect,render
from django.views import View
from .models import Product, Cart
from .forms import ProductSearchForm, QueryForm, RegisterForm, LoginForm
from .extras import full_text_search
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_API_KEY

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
    
    def post(self, request, pk):
        cart_list = Cart.objects.filter(product_id=pk, user=request.user).first()
        if not cart_list:
            inst = Cart.objects.create(product_id=pk, user=request.user)
            inst.save()
        else:
            cart_list.quantity += 1
            cart_list.save()
            
        return HttpResponseRedirect(f"/product/{pk}")
    
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
        
class CartView(View):
    template_name = "healthy_hunger/cart.html"

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login/")
        products = [prod for prod in request.user.cart_orders.all()]
        total_price = sum([prod.product.price * prod.quantity for prod in products])
        context={
            "products":products,
            "total_price":total_price
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        total_value = int(float(request.POST["total_value"])) * 100

        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': 'Food',
                        },
                        'unit_amount': total_value,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:7000/',
            cancel_url='http://localhost:7000/',
        
        )

        return HttpResponseRedirect(f"{session.url}")