from typing import Collection
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
import datetime


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Dish(models.Model):

    # course
    Starter = "ST"
    Main = "MA"
    Dessert = "DE"

    # Dietry 
    Meat = "ME"
    Fish = "FI"
    Vegetarian = "VE"

    course_type = [(Starter, "Starter"), (Main, "Main"), (Dessert, "Dessert")]
    dietry_type = [(Meat, "Meat"), (Fish, "Fish"), (Vegetarian, "Vegetarian")]

    course = models.CharField(max_length = 2, choices= course_type, default = "ST")
    name = models.CharField(max_length= 150)
    diet = models.CharField(max_length = 2, choices= dietry_type, blank = True)
    price = models.FloatField(validators=[MinValueValidator(0.00)], default=0.00)

    def __str__(self):
        return self.name

class Order(models.Model):

    #Status
    Ordering = "OR"
    Pending = "PE"
    Delivery = "DL"
    Collect = "CL"
    Complete = "CO"

    #Delivery
    Delivery = "DL"
    Collection = "CL"

    status_type = [(Ordering, "Ordering"),(Pending, "Pending"), (Delivery, "Out for Delivery"), (Collect, "Ready for Collection"), (Complete, "Complete")]
    delivery_type = [(Delivery, "Delivery"),(Collection, "Collection")]

    time = models.DateTimeField(auto_now_add = True, editable= False)
    order_code = models.CharField(max_length=6, primary_key=True, editable=False, unique=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default = id(CustomUser))
    starter  = models.ForeignKey(Dish, on_delete=models.PROTECT, limit_choices_to={'course': "ST"}, related_name='starter', blank = True, null = True)
    main = models.ForeignKey(Dish, on_delete=models.PROTECT, limit_choices_to={'course': "MA"}, related_name='main', blank = True, null = True)
    dessert = models.ForeignKey(Dish, on_delete=models.PROTECT, limit_choices_to={'course': "DE"}, related_name='dessert', blank = True, null = True)
    delivery = models.CharField(max_length = 2, choices= delivery_type, default = "Y")
    status = models.CharField(max_length = 2, choices= status_type, default = "OR")

    @property
    def get_total(self):
        total = self.starter.price + self.main.price + self.dessert.price
        if self.delivery == "DL":
            total += 3
        return total

    def save(self, *args, **kwargs):
        if not self.order_code:
           self.order_code = get_random_string(6)
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
     return self.order_code




   

