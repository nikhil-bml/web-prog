from django.shortcuts import HttpResponseRedirect,render
from django.views import View

class Home(View):
    template_name = "healthy_hunger/home.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
