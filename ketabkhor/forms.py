from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=32, required=True)
    firstname = forms.CharField(label='نام', max_length=32, required=True)
    lastname = forms.CharField(label='نام خانوادگی', max_length=64, required=True)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(), min_length=6, required=True)
    password_r = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(), min_length=6, required=True)
    email = forms.EmailField(label='ایمیل', required=True)
    birthday = forms.DateField(label='تاریخ تولد')

    def clean_password_r(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_r')
        if password1 != password2:
            raise forms.ValidationError('رمز عبور و تکرار رمز عبور، هم‌خوانی ندارند!')
        return password2
