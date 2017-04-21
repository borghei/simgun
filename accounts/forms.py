from django import forms
from django.contrib.auth import authenticate


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=64, required=True)
    firstname = forms.CharField(label='نام', max_length=64, required=True)
    lastname = forms.CharField(label='نام خانوادگی', max_length=128, required=True)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(), min_length=6, required=True)
    password_r = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(), min_length=6, required=True)
    email = forms.EmailField(label='ایمیل', required=True)
    # birthday = forms.DateField(label='تاریخ تولد')

    def clean_password_r(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_r')
        if password1 and password1 != password2:
            raise forms.ValidationError('رمز عبور و تکرار رمز عبور، هم‌خوانی ندارند!')
        return password2


class UserLogin(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=64, required=True)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            if not user:
                raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است")
            if not user.check_password(password):
                raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است")
            if not user.is_active:
                raise forms.ValidationError("حساب کاربری شما فعال نیست")
        return super(UserLogin, self).clean()
