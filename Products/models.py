from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to='category', null=True, blank=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='products', null=True, blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  base_price = models.DecimalField(max_digits=10, decimal_places=2)
  Category = models.ForeignKey(Category, on_delete=models.CASCADE)
  in_stock = models.BooleanField(default=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'