from django.db import models

# Create your models here.

class product(models.Model):
    p_name = models.CharField(max_length=50)
    des_CHOICES = (
        ('Product1', 'Product1'),
        ('Product2', 'Product2'),
        ('Product3', 'Product3'),
        ('Product4', 'Product4'),
        ('Product5', 'Product5'),
    )
    p_choices = models.CharField(max_length=50,choices=des_CHOICES,default='ASSOCIATE')
    p_quantity = models.CharField(max_length=100)
    p_images = models.ImageField(upload_to='product_images/')
    p_images_1 = models.ImageField(upload_to='product_images_1/')
    p_images_2 = models.ImageField(upload_to='product_images_2/')

    def __str__(self):
        return self.p_name
    
    class Meta:
        db_table = 'product'
