from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length= 200,null=True)
    email= models.EmailField()
    sub= models.CharField(max_length=200,null=True)
    message= models.CharField(max_length= 200,null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    image=models.FileField(upload_to='product/',blank=True, null=True)
    image1=models.FileField(upload_to='product/',blank=True, null=True)
    image2=models.FileField(upload_to='product/',blank=True, null=True)
    image3=models.FileField(upload_to='product/',blank=True, null=True)
    name = models.CharField(max_length=100,null=False,blank=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,default=False,null=True)
    description = models.TextField()
    percentage=models.CharField(max_length=100,null=True)
    dell=  models.SmallIntegerField(default=0,null=False,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"

class CartItem(models.Model):
    image=models.FileField(upload_to='cart/',blank=True, null=True)
    cart = models.ForeignKey(Cart, related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.user.username}"

STATE_CHOICES = (
('Himachal','Himachal'),
('Chandigarh','Chandigarh'),
('Punjab','Punjab'),
('Haryana', 'Haryana'),
('Delhi', 'Delhi'),
('Uttar Pradesh', 'Uttar Pradesh'),
('Rajasthan', 'Rajasthan'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Gujarat', 'Gujarat'),
('Maharashtra', 'Maharashtra'),
('Karnataka', 'Karnataka'),
('Andhra Pradesh', 'Andhra Pradesh'),
('Telangana', 'Telangana'),
('Tamil Nadu', 'Tamil Nadu'),
('Kerala', 'Kerala'),
('Odisha', 'Odisha'),
('West Bengal', 'West Bengal'),
('Bihar', 'Bihar'),
('Jharkhand', 'Jharkhand'),
('Assam', 'Assam'),
('Meghalaya', 'Meghalaya'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Sikkim', 'Sikkim'),
('Nagaland', 'Nagaland'),
('Mizoram', 'Mizoram'),
('Manipur', 'Manipur'),
('Tripura', 'Tripura'),
('Uttarakhand', 'Uttarakhand'),
)
class Customer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	locality = models.CharField(max_length= 200)
	city = models.CharField(max_length = 50)
	zipcode = models.IntegerField()
	state = models.CharField(choices = STATE_CHOICES, max_length = 50)

	def __str__(self):
		return str(self.id)




