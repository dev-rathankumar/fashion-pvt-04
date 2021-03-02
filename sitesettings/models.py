from django.db import models
from accounts.models import Business, User


class Header(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=500)
    site_logo = models.ImageField(upload_to='logos', blank=True)
    favicon = models.ImageField(upload_to='logos', blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.business


# class Banner(models.Model):
#     business = models.ForeignKey(Business, on_delete=models.CASCADE)
#     created_date    = models.DateTimeField(auto_now_add=True)
#     modified_date   = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.business
#
#
# class BannerImage(models.Model):
#     align_choice = (
#         ('left', 'left'),
#         ('center', 'center'),
#         ('right', 'right'),
#     )
#     banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
#     banner_image = models.ImageField(upload_to='banner_images', blank=True)
#     title = models.CharField(max_length=500, null=True, blank=True)
#     sub_title = models.CharField(max_length=500, null=True, blank=True)
#     button_name = models.CharField(max_length=20, null=True, blank=True)
#     content_align = models.CharField(max_length=10,choices=align_choice, default='center')
#
#     def __str__(self):
#         return self.business

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
