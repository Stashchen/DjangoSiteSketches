from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=250)
    article = models.CharField(max_length=25, default='-')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    

    def __str__(self):
        return self.name


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/images')
    
    def __str__(self):
        return self.product.name
    
    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)
