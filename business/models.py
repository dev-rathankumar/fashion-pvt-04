from django.db import models
from accounts.models import Business

# Image manipulation
from io import BytesIO
from PIL import Image
from django.core.files import File

from ckeditor.fields import RichTextField


# website settings

# Image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image

# def upload_to(instance, filename):
#     return 'business/%s/images/%s' % (instance.business.user.username, filename)

class SiteSetting(models.Model):
    business   = models.ForeignKey(Business, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=255)
    site_logo  = models.ImageField(upload_to='logos', blank=True, max_length=500)
    copyright  = RichTextField(blank=True)

    # Override save method
    def save(self, *args, **kwargs):
        new_image = compress(self.site_logo)
        self.site_logo = new_image
        super(SiteSetting, self).save(*args, **kwargs)
        img = Image.open(self.site_logo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.site_logo.path)
        super(SiteSetting, self).save(*args, **kwargs)

    def __str__(self):
        return self.site_title


class TestRathan(models.Model):
    business_test   = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True)
    site_title = models.CharField(max_length=255)

    def __str__(self):
        return self.site_title
