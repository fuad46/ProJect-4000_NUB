from django.db import models


# Create your models here.
class CartProduct(models.Model):
  cart = models.ForeignKey('Orders.Cart', on_delete=models.CASCADE)
  product = models.ForeignKey('Products.Product', on_delete=models.CASCADE)
  quantity = models.PositiveBigIntegerField(default=1)
  unit = models.CharField(max_length=10, default='pcs')

  def __str__(self):
    return f'{self.product.name} in {self.cart.user}\'s Cart'


class Cart(models.Model):
  user = models.OneToOneField('Users.Customer', on_delete=models.CASCADE)
  products = models.ManyToManyField('Products.Product', through=CartProduct)

  def __str__(self):
    return f'{self.user.username}\'s cart'
  
  class Meta:
    verbose_name = 'Cart'
    verbose_name_plural = 'Carts'
