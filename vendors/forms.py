from django.forms import ModelForm
from product.models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ['title', 'category', 'price', 'weight', 'itemCount', 'description', 'mainPic']
        exclude = ("category",)
        labels = {
            'title': 'عنوان',
            'category': 'موضوع',
            'price': 'قیمت',
            'weight': 'وزن(کیلوگرم)',
            'itemCount': 'تعداد',
            'description': 'توضیحات',
            'mainPic': 'عکس اصلی'
        }
    #
    # def clean(self):
    #     cleaned_data = super(TransferCreationForm, self).clean()
    #     source = cleaned_data.get('source')
    #     destination = cleaned_data.get('destination')
    #     amount = cleaned_data.get('amount')
    #
    #     if source.ban_status:
    #         self.add_error('source', 'حساب موردتظر مسدود شده است.')
    #     elif source.closed_by_customer:
    #         self.add_error('source', 'حساب موردتظر توسط کاربر بسته شده است.')
    #
    #     if destination.ban_status:
    #         self.add_error('destination', 'حساب موردتظر مسدود شده است.')
    #     elif destination.closed_by_customer:
    #         self.add_error('destination', 'حساب موردتظر توسط کاربر بسته شده است.')
    #
    #     if amount + SiteSettings.load().transfer_surcharge > source.balance:
    #         self.add_error('amount', 'مبلغ وارد شده از موجودی حساب بیشتر است.')