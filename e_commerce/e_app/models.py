from django.db import models

# Create your models here.

class product(models.Model):
    p_name = models.CharField(max_length=50,primary_key=True)
    des_CHOICES = (
        ('Product1', 'Product1'),
        ('Product2', 'Product2'),
        ('Product3', 'Product3'),
        ('Product4', 'Product4'),
        ('Product5', 'Product5'),
    )
    p_choices = models.CharField(max_length=50,choices=des_CHOICES,default='Product1')
    p_quantity = models.CharField(max_length=100)
    p_price = models.DecimalField(max_digits=10,decimal_places=2)
    p_images = models.ImageField(upload_to='product_images/')
    p_images_1 = models.ImageField(upload_to='product_images_1/')
    p_images_2 = models.ImageField(upload_to='product_images_2/')

    def __str__(self):
        return self.p_name
    
    class Meta:
        db_table = 'product'

class cartitems(models.Model):
    cart_product=models.ForeignKey(product, on_delete=models.CASCADE)
    cart_quantity=models.PositiveIntegerField(default=0)
    cart_price=models.DecimalField(max_digits=10,decimal_places=2)
    cart_images = models.ImageField(upload_to='cart_images/')
    data_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'self.cart_product'
    
    class Meta:
        db_table = 'cartitems'