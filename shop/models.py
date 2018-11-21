from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
<<<<<<< HEAD
import django_filters

=======
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db
SIZE_CHOICES = [(j, str(j)) for j in ['XS','S','M','L','XL','XXL']]
COLOR_CHOICES = [(k, str(k)) for k in ['Green','Blue','Red','Orange','Yellow','Black','White']]

#COLOR_CHOICES = (
    #('Green','GREEN'),
    #('Blue','BLUE'),
    #('Red','RED'),
    #('Orange','ORANGE'),
    #('Black','BLACK'),
    #('Yellow','YELLOW'),
    #('White','WHITE')
#)
#SIZE_CHOICES = (
    #('XS','XS'),
    #('S','S'),
    #('M','M'),
    #('L','L'),
    #('XL','XL'),
    #('XXL','XXL')
#)
class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category',
                           args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default='L')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='green')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail',
                           args=[self.id, self.slug])
<<<<<<< HEAD

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'price']
=======
>>>>>>> dc0b92a691b20f4bfd343a495d8e0c2d24f472db
