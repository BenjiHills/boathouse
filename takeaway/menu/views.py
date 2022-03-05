from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.db.models import Case, When, Value

def form_valid(self, form):
  form.instance.user = self.request.user
  return form_valid(form)

class AccountCreateView(CreateView):
  
    #Allows the User to Create a New Account
   
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('/')

class HomeView(ListView):
    model = Dish
    template_name = "menu/home.html"


    def get_queryset(self,):
        qs = super().get_queryset()
        return qs.order_by( Case( 
                      When ( diet="ME", then=Value(0) ),
                      When ( diet="FI", then=Value(1)  ),
                      default = Value(2)
        )
        )

class CreateOrderView(CreateView):
    model = Order
    template_name = "menu/create.html"
    form_class = OrderCreateForm
    
    def get_success_url(self):
        return reverse_lazy('checkout', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)



class CheckoutView(UpdateView):
    model = Order
    template_name = "menu/checkout.html"
    form_class = CheckoutForm 
    success_url = "/"

    def form_valid(self, form):
        if self.request.method=='POST' and 'Order' in self.request.POST:
            form.instance.status = "PE"
        return super().form_valid(form)

class DishView(CreateView):
    model = Dish
    template_name = "menu/dishes.html"
    form_class = CreateDishForm 
    success_url = "/dishes"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = self.model.objects.exclude(course = "EM").order_by("-course", "name")
        return super(DishView, self).get_context_data(**kwargs)
    
    def form_valid(self, form):
        form.instance.name = form.instance.name.title()
        form.instance.descrip = form.instance.descrip.capitalize()
        return super().form_valid(form)

class CustomerOrderView(ListView):
    model = Order
    template_name = "menu/orders.html"

    def get_queryset(self):
        return Order.objects.filter(status__in = ["PE", "DL", "CL"]).order_by("time")

  
class StatusUpdateView(UpdateView):
    model = Order
    template_name = "menu/order_status.html"
    form_class = OrderStatusForm
    success_url = "/orders"

    def form_valid(self, form):
        if self.request.method=='POST' and 'Delivery' in self.request.POST:
            form.instance.status = "DL"
        elif self.request.method=='POST' and 'Collection' in self.request.POST:
            form.instance.status = "LL"
        elif self.request.method=='POST' and 'Complete' in self.request.POST:
            form.instance.status = "CO"
         
        return super().form_valid(form)

class MyOrderView(ListView):
        model = Order
        template_name = "menu/my_orders.html"

        def get_queryset(self):
            return Order.objects.filter(customer = self.request.user).order_by("-time")

class DishDeleteView(DeleteView): 
        model = Dish
        template_name = "menu/dish_delete.html"
        success_url = "/dishes"

class DishUpdateView(UpdateView):
    model = Dish
    template_name = "menu/dish_update.html"
    form_class = DishUpdateForm 
    success_url = "/dishes"

class OrderDeleteView(DeleteView): 
        model = Order
        template_name = "menu/order_delete.html"
        success_url = "/"


