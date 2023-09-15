from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from magazin_app.models import Order
from unicodedata import decimal
from .models import User, Order, Product


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def my_view(request):
    context = {"name": "John"}
    return render(request, "magazin_app/index.html", context)


class TemplIf(TemplateView):
    template_name = "magazin_app/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.kwargs['id_user'])
        orders = Order.objects.filter(user=user).all()
        context['order'] = orders
        return context
