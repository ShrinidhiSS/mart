
from PIL import Image
from django.db import models

type = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Girls', 'Girls'),
    ('Boys', 'Boys'),
)


class Product(models.Model):
    product_name = models.CharField(max_length=50, default='Unknown')
    product_price = models.IntegerField(default=100)
    product_image = models.ImageField(default='default.jpg', upload_to='product_pics')
    category_name = models.CharField(max_length=50, choices=type, default='Unknown')

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.product_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.product_image.path)

# class Men(models.Model):
#     pass

from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_image = models.ImageField()
