from django.db import models
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from accounts.models import Business


class Category(MPTTModel):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(max_length=1000, blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'blog category'
        verbose_name_plural = 'blog categories'

    def __str__(self):
        return self.category_name

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        full_path = [self.category_name]
        k = self.parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.parent
        return ' / '.join(full_path[::-1])


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='blog/uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=300)
    blog_body = RichTextField()
    author = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('blog_detail', args=[self.category.slug, self.slug])
