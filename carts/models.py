from django.db import models
from products.models import Product, Variants
from accounts.models import Business, User
from django.forms import ModelForm



# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL,blank=True, null=True) # relation with varinat
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.product_name

    @property
    def price(self):
        return (self.variant.price)

    @property
    def size(self):
        return (self.variant.size)

    @property
    def color(self):
        return (self.variant.color)

    @property
    def amount(self):
        return (self.quantity * self.variant.price)

    @property
    def varamount(self):
        return (self.quantity * self.variant.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    note = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product


class Tax(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE, unique=True)
    tax_percentage = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Tax (%)")

    class Meta:
        verbose_name = 'tax'
        verbose_name_plural = 'tax'

    def __unicode__(self):
        return self.tax_percentage
