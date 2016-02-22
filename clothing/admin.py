# coding:utf-8
from django import forms
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple
from clothing.models import *


class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline, ]


class AttrValueInline(admin.StackedInline):
    model = AttrValue
    extra = 1
    ordering = ('name',)
    # filter_horizontal = ('category', )  # 多选水平排列


class AttrAdmin(admin.ModelAdmin):
    inlines = [AttrValueInline, ]


class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('attrvalue', )  # 多选水平排列


class ImgAdminInline(admin.StackedInline):
    model = Img
    # fk_name = 'good'
    extra = 0


class GoodSkuAdminInline(admin.StackedInline):
    model = GoodSku
    extra = 0
    # readonly_fields = ('sc',)  # 只读字段
    # fields = ('sc',)
    # filter_horizontal = ('image',)


class GoodSkuAdmin(admin.ModelAdmin):
    list_display = ['good', 'cs']


class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodSkuAdminInline]
    filter_horizontal = ('attrvalue', 'tag')  # 多选水平排列
    readonly_fields = ('prices', 'sales', 'nums')
    # form = 'AttrValueForm'
    # formfield_overrides = {
    # models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }  # 这个可用,这个字段变成了复选框形式


class SellingAdmin(admin.ModelAdmin):
    ##################
    # 这部分也可以写在model中
    # def total_price(self, obj):
    # # ModelAdmin中的方法会得到两个参数,第一个是类本身的一个实例(app.GoodsClassAdmin),第二个是这个类管理的模型实例(GoodsClass)
    # return obj.count * obj.price
    # total_price.short_description = '小计'
    ##################

    readonly_fields = ('goodsku', 'count', 'price', 'total_price')
    # form = 'AttrValueForm'
    # formfield_overrides = {
    # models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }  # 这个可用,这个字段变成了复选框形式


class SellingAdminInline(admin.StackedInline):
    model = Selling
    extra = 0
    # readonly_fields = ('sc',)  # 只读字段
    # fields = ('sc',)
    # filter_horizontal = ('image',)


class OrderAdmin(admin.ModelAdmin):
    inlines = [SellingAdminInline]
    # filter_horizontal = ('attrvalue', 'tag')  # 多选水平排列
    # readonly_fields = ('prices', 'sales', 'nums')
    # form = 'AttrValueForm'
    # formfield_overrides = {
    # models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }  # 这个可用,这个字段变成了复选框形式


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Cart)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Tag)
admin.site.register(Good, GoodAdmin)
admin.site.register(GoodSku, GoodSkuAdmin)
admin.site.register(Attr, AttrAdmin)
admin.site.register(AttrValue)
admin.site.register(Color)
admin.site.register(Ad)
admin.site.register(Selling, SellingAdmin)
admin.site.register(Order, OrderAdmin)