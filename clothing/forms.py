# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from clothing.models import *


class LoginForm(forms.Form):
    # 用户名字段
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "请输入用户名", "required": "required"}),
        # 使用type="text",增加了一个属性 "placeholder"="请输入用户名","required": "required"
        required=True,  # required参数表示必须填写,验证时会验证不为空,
        min_length=3,
        max_length=30,  # min_length, max_length 都是用来验证最小和最大长度.
        error_messages={"required": "必须输入用户名",
                        "min_length": "用户名太短",
                        "max_length": "用户名太长"})  # 当验证出错的时候,给出这里的提示信息.
    # 渲染成html :<input id="id_username" maxlength="50" name="username" placeholder="请输入用户名" required="required" type="text">
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "请输入密码"}),
        required=True,
        min_length=3,
        max_length=20,
        error_messages={"required": "必须输入密码",
                        "min_length": "密码太短",
                        "max_length": "密码太长"})


class AddressForm(forms.ModelForm):
    # 收件人
    class Meta:
        model = UserProfile
        fields = ['recipients', 'qq', 'tel', 'address']
    pass


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "请输入用户名", "required": "required"}),
        required=True,
        min_length=3,
        max_length=30,
        error_messages={"required": "必须输入用户名",
                        "min_length": "用户名太短",
                        "max_length": "用户名太长"})
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "请输入邮箱", "required": "required"}),
        required=True,
        error_messages={"required": "必须输入邮箱", })
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "确认密码", "required": "required", }),
        min_length=3,
        max_length=20,
        error_messages={"required": "不能为空", })
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required", }),
        min_length=3,
        max_length=20,
        error_messages={"required": "不能为空", })

    def clean_username(self):
        # 单独验证字段,clean_ 开头 后面加字段名
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username  # 没有问题返回字段本身
        raise forms.ValidationError(u'%s 用户名已经存在' % username)
        # 有问题就抛出ValidationError错误
        # 在模版中使用{{<form对象>.errors.<字段名>}}来获得错误信息.

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'%s 邮箱已经存在' % email)

    def clean_password(self):
        if self.cleaned_data['confirm_password'] == self.cleaned_data['password']:
            return self.cleaned_data['password']
        raise forms.ValidationError(u'两次输入密码不一致')


# class AddCartForm(forms.ModelForm):
#     class Meta:
#         model = Cart
#         fields = ['goodsku', 'count', 'selected', 'user']