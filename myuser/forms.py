import unicodedata
from django import forms
from django.contrib.auth import authenticate, password_validation, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from .models import allUser


class BlogUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    https://github.com/django/django/blob/master/django/contrib/auth/forms.py
    """
    error_messages = {
        'password_mismatch': "两次密码不相符,请重新填写",
        'duplicate_username': "这个用户名已经有人注册过了，请更换",
        'duplicate_email': "这个邮箱已经被注册过了",
        'duplicate_phone': "这个手机号已经被注册过了",
    }

    # 包含字母、数字和字符@/./+/-/_
    username = forms.RegexField(
        label='用户名',
        regex=r'^[\w.@+-]+$',
        max_length=20,
        error_messages={
            'required': "用户名未输入",
            'invalid': "用户名不合法",
        },
        widget=forms.TextInput(attrs={'class': 'color-form-control'}),
        help_text='请输入您想要的用户名',
    )

    password1 = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'color-form-control'}),
        help_text='请输入您的新密码',
        error_messages={
            'required': "密码未输入",
        },
    )
    password2 = forms.CharField(
        label="密码确认",
        widget=forms.PasswordInput(attrs={'class': 'color-form-control'}),
        strip=False,
        help_text="请输入与上面一样的密码",
        error_messages={
            'required': "未输入密码确认",
        }
    )

    email = forms.EmailField(
        label="邮箱",
        widget=forms.EmailInput(attrs={'class': 'color-form-control'}),
        error_messages={
            'invalid': "email格式不正确",
            'required': "email未输入",
            'duplicate_email': "这个邮箱已经被注册过了",
        }
    )

    phone = forms.RegexField(
        label="手机号",
        max_length=15,
        regex=r'^[0-9]+$',
        error_messages={
            'invalid': "电话格式不对",
            'required': "未输入手机号",
            'duplicate_phone': "这个手机号已经被注册过了",
        },
        widget=forms.TextInput(attrs={'class': 'color-form-control'}),
    )

    class Meta:
        model = allUser
        fields = ('username', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    # 直接从源码仿过来的
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        existed_email = allUser.objects.filter(email=email).exists()
        if not existed_email:
            return email
        else:
            raise forms.ValidationError(
                self.error_messages['duplicate_email'],
                code='duplicate_email',
            )

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        existed_phone = allUser.objects.filter(phone=phone).exists()
        if not existed_phone:
            return phone
        else:
            raise forms.ValidationError(
                self.error_messages['duplicate_phone'],
                code='duplicate_phone',
            )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        existed = allUser.objects.filter(username=username).exists()
        # existed_username = allUser.objects.values_list('username')
        if not existed:
            return username
        else:
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.ClearableFileInput())

    class Meta:
        model = allUser
        fields = ('avatar',)
