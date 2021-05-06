from django.db import models
from accounts.models import Business, User
from PIL import Image
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class Header(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=500)
    site_logo = models.ImageField(upload_to='logos', blank=True)
    favicon = models.ImageField(upload_to='logos', blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.business


class Homepage(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business.company_name


class BannerImage(models.Model):
    align_choice = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    )
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE)
    banner_image = models.ImageField(upload_to='banner_images', blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    sub_title = models.CharField(max_length=500, null=True, blank=True)
    button_name = models.CharField(max_length=20, null=True, blank=True)
    button_link = models.CharField(max_length=255, null=True, blank=True)
    button_color = ColorField(default='#000000')
    content_align = models.CharField(max_length=10, choices=align_choice, default='center')

    def __str__(self):
        return self.title


class StoreFeature(models.Model):
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='store_feature_icons', blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)
    sub_title = models.CharField(max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.icon.path)

        if img.height > 80 or img.weight > 80:
            output_size = (80,80)
            img.thumbnail(output_size)
            img.save(self.icon.path)


    def __str__(self):
        return self.title


class ParallaxBackground(models.Model):
    btn_align_choice = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    )
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE)
    parallax_image = models.ImageField(upload_to='parallax_image', blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = RichTextField(max_length=1000, null=True, blank=True)
    button_name = models.CharField(max_length=20, null=True, blank=True)
    button_link = models.CharField(max_length=500, null=True, blank=True)
    button_color = ColorField(default='#000000')
    content_align = models.CharField(max_length=10, choices=btn_align_choice, default='center')

    def __unicode__(self):
        return self.title


class Footer(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    footer_credit = models.CharField(max_length=250)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business


class ContactPage(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business
