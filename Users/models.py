from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group,Permission
# Create your models here.

class Customer(AbstractUser):
  phone = models.CharField(max_length=15)
  shipping_address = models.TextField(null=True, blank=True)
  billing_address = models.TextField(null=True, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

  groups = models.ManyToManyField(
    Group,
    related_name='customer_set',
    blank=True,
    help_text="The grroups this user belongs to.",
    verbose_name="groups"
  )
  user_permissions = models.ManyToManyField(
    Permission,
    related_name='customer_set',
    blank=True,
    help_text="Specific Pemission for this user.",
    verbose_name="user permissions"
  )
  def __str__(self):
    return f'{self.username}'
  
  class Meta:
    verbose_name = 'Customer'
    verbose_name_plural = 'Customers'