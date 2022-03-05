from django.db import models
from django.db.models import Q
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
    Empty = "EM"
    Starter = "ST"
    Main = "MA"
    Dessert = "DE"

    # Dietry 
    Meat = "ME"
    Fish = "FI"
    Vegetarian = "VE"

    course_type = [(Empty, " "), (Starter, "Starter"), (Main, "Main"), (Dessert, "Dessert")]
    dietry_type = [(Meat, "Meat"), (Fish, "Fish"), (Vegetarian, "Vegetarian")]

    course = models.CharField(max_length = 2, choices= course_type, default = "ST")
    name = models.CharField(max_length= 50, blank =True)
    descrip= models.CharField(max_length= 150, blank =True, verbose_name= "description")
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
    starter  = models.ForeignKey(Dish, on_delete=models.SET_DEFAULT, limit_choices_to= Q(course = "ST") | Q(course = "EM"), related_name='starter', default= id(1))
    main = models.ForeignKey(Dish, on_delete=models.CASCADE, limit_choices_to=Q(course = "MA") | Q(course = "EM"), related_name='main', default= id(1))
    dessert = models.ForeignKey(Dish, on_delete=models.CASCADE, limit_choices_to=Q(course = "DE") | Q(course = "EM"), related_name='dessert', default= id(1))
    delivery = models.CharField(max_length = 2, choices= delivery_type, default = "DL")
    status = models.CharField(max_length = 2, choices= status_type, default = "OR")

    @property
    def get_total(self):
        prices =[self.starter.price, self.main.price, self.dessert.price]
        total = 0
        for price in prices:
                total += price
        if self.delivery == "DL":
            total += 3
        return total

    def save(self, *args, **kwargs):
        if not self.order_code:
           self.order_code = get_random_string(6)
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
     return self.order_code




   

