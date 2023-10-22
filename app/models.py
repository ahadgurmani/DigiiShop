from django.db import models
from django.contrib.auth.models import User

catagory_choose = (
    ('lap', 'laptops'),
    ('mob', 'Mobile'),
)
class Product(models.Model):
    title = models.CharField(max_length= 200)
    price = models.FloatField()
    brand = models.CharField(max_length= 200)
    description = models.TextField()
    image = models.ImageField(upload_to= "productimg")
    catagory = models.CharField(choices= catagory_choose, max_length=4)
    def __str__(self):
        return self.title

choose_catagory = (
    ('Lahore', 'lahore'),
    ('Karachi', 'karachi'),
    ('Islamabad', 'islamabad'),
    ('Faisalabad', 'faisalabad'),
    ('Multan', 'multan'),
    ('Bahawalpur', 'bahawalpur'),
    ('Layyah', 'layyah'),
)
class Costumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 333)
    city = models.CharField(choices= choose_catagory, max_length=20)
    locality = models.CharField(max_length= 100)
    father_name = models.CharField(max_length= 100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)
    def __str__(self):
        return self.id












# Create your models here.