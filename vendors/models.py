from django.db import models

from accounts.models import Vendor
from product.models import Product
from buying.models import ShoppingbagAddress


class BookVendor(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vendor) + ' - ' + str(self.book)


class ShoppingbagVendor(ShoppingbagAddress):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)