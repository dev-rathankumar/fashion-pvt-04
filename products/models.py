from django.db import models
from category.models import Category
from business.models import Business
from accounts.models import User
from django.urls import reverse
from django.forms import ModelForm

# Image manipulation
from io import BytesIO
from PIL import Image
from django.core.files import File

from django.utils.safestring import mark_safe

# Image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image

class Product(models.Model):
    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    business        = models.ForeignKey(Business, on_delete=models.CASCADE)
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    image           = models.ImageField(upload_to='store/products/%Y/%m/%d')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    variant         = models.CharField(max_length=10,choices=VARIANTS, default='None')
    is_new_arrival  = models.BooleanField(default=False, blank=True)
    is_popular      = models.BooleanField(default=False, blank=True)
    is_active       = models.BooleanField(default=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)


    # Override save method
    def save(self, *args, **kwargs):
        # new_image = compress(self.image)
        # self.image = new_image
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])



class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='store/products/%Y/%m/%d', max_length=5000)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'



class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    def __str__(self):
        return self.name
    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


# PRODUCT VARIATION
class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)
    image_id = models.IntegerField(blank=True,null=True,default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    def __str__(self):
        return self.title

    def image(self):
        img = ProductGallery.objects.get(id=self.image_id)
        if img.id is not None:
             varimage=img.image.url
        else:
            varimage=""
        return varimage

    def image_tag(self):
        img = ProductGallery.objects.get(id=self.image_id)
        if img.id is not None:
             return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL,blank=True, null=True)
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
        return (self.quantity * self.product.price)

    @property
    def varamount(self):
        return (self.quantity * self.variant.price)


class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['quantity']
