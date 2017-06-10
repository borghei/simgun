from django.db import models

from accounts.models import Vendor
from product.models import Product
# from buying.models import


class ProductVendor(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vendor) + ' - ' + str(self.product)

#
# class ShoppingbagVendor(ShoppingbagAddress):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)