from django.db import models
from accounts.models import UserProfile

from product.models import Product
from buying.models import Address


class Bag(models.Model):
    address = models.ForeignKey(Address, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.IntegerField(choices=((0, 'باز'), (1, 'بسته')), default=0)

    def get_sum_price(self):
        return sum(s.get_sum() for s in self.shoppingbagproduct_set.all() if s.status == 0)


class ShoppingbagProduct(models.Model):
    bag = models.ForeignKey(Bag, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    sb_choices = ((-2, 'به دستم نرسیده'), (-1, 'عدمم پشتیبانی شهر'), (0, 'در لیست خرید'), (1, 'سفارش به دست ارائه دهنده رسیده'),
                  (2, 'ارسال شده'), (3, 'به دستم رسیده'))
    status = models.IntegerField(choices=sb_choices, default=0)

    def get_stat(self):
        return self.sb_choices[self.status+2][1]

    def get_sum(self):
        return self.price*self.product_count


