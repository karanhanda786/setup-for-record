from django.db import models
import datetime
from django.urls import reverse
# Create your models here.
class ProductInfo(models.Model):
    product_name = models.CharField(max_length=200)
    Created_at =  models.DateTimeField(editable=False)
    expire_at = models.DateField(auto_now=False, auto_now_add=False)
    Company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.Created_at = datetime.datetime.today()
        return super(ProductInfo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('expires:detailProduct')

    class Meta:
        ordering = ['-Created_at']
