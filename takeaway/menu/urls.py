from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.AccountCreateView.as_view(), name="signup"),
    path("", views.HomeView.as_view(), name="home"),
    path("create/", views.CreateOrderView.as_view(), name="create"),
    path("checkout/<pk>", views.CheckoutView.as_view(), name = "checkout"),
    path("dishes/", views.DishView.as_view(), name="dishes"),
    path("orders/", views.CustomerOrderView.as_view(), name="orders"),
    path("order_status/<pk>", views.StatusUpdateView.as_view(), name="order_status"),
    path("my_orders/", views.MyOrderView.as_view(), name="myorders"),
    path("dishes/delete/<pk>", views.DishDeleteView.as_view(), name="dish_delete"),
    path("checkout/cancel/<pk>", views.OrderDeleteView.as_view(), name="order_delete"),
    path("dishes/update/<pk>", views.DishUpdateView.as_view(), name = "dish_update"),

]