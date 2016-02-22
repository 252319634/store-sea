# coding: utf-8
import datetime
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import sys
from django.utils.timezone import now

reload(sys)
sys.setdefaultencoding("utf-8")
# UnicodeEncodeError
class UserProfile(models.Model):
    """
    用户类,扩展User
    """
    user = models.OneToOneField(User, primary_key=True)
    recipients = models.CharField(max_length=20, default='', blank=True, verbose_name='收件人')
    qq = models.CharField(max_length=20, default='', blank=True, verbose_name='QQ号码')
    tel = models.CharField(max_length=20, default='', blank=True, verbose_name='手机号码')
    address = models.CharField(max_length=200, default='', blank=True, verbose_name='地址')
    view_history = models.CommaSeparatedIntegerField(max_length=10, default='', null=True, verbose_name='浏览记录')
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Cart(models.Model):
    """
    购物车,衣服的列表
    """
    user = models.ForeignKey(User, verbose_name='用户')
    goodsku = models.ForeignKey('GoodSku', verbose_name='商品')
    count = models.IntegerField(default=1, verbose_name='数量')
    selected = models.BooleanField(default=False, verbose_name='是否结算')

    def sum_price(self):
        return self.goodsku.new_price * self.count

    def __str__(self):
        return "用户%s选购:%s,%s件" % (self.user.username, self.goodsku.good.name, self.count)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'


class Order(models.Model):
    """
    订单,包含订单号,下单时间,下单用户,总价格,收货地址
    """
    user = models.ForeignKey(User, verbose_name='用户')
    orderid = models.CharField(max_length=100, null=True, verbose_name='订单号')
    time = models.DateTimeField(auto_now=True, null=True, verbose_name='销售时间')
    address = models.CharField(max_length=200, null=True, verbose_name='收货信息')
    total_price = models.FloatField(default=0.0, null=True, verbose_name='总金额')

    def __str__(self):
        return "%s,%s" % (self.user.username, self.orderid)

    def _total_price(self):
        selling_set = self.selling_set.all()
        totalp = 0
        for s in selling_set:
            totalp += s.count * s.price
        return totalp

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class Selling(models.Model):
    """
    销售记录
    """
    order = models.ForeignKey('Order', verbose_name='订单号')
    goodsku = models.ForeignKey('GoodSku', verbose_name='商品')
    count = models.IntegerField(verbose_name='数量')
    price = models.FloatField(default=0.0, verbose_name='单价')


    def total_price(self):
        # 这个方法也可以写在admin中
        # ModelAdmin中的方法会得到两个参数total_price(self,obj)
        # 第一个是类本身的一个实例(app.GoodsClassAdmin)
        # 第二个是这个类管理的模型实例(GoodsClass)
        return self.count * self.price

    total_price.short_description = '小计'

    def __str__(self):
        return "%s购买%s,数量%s个,单价%s" % (self.order.user.username, self.goodsku.good.name, self.count, self.price)

    def save(self, *args, **kwargs):
        """
        重写save方法,保存时更新商品的 价格,销量,库存 为sku的统计后的数据
        """
        super(self.__class__, self).save(*args, **kwargs)  # 先保存一下销售记录
        self.order.total_price = self.order._total_price()
        self.order.save()  # 更新商品的信息

    class Meta:
        verbose_name = '销售记录'
        verbose_name_plural = verbose_name


class Ad(models.Model):
    """
    广告图片轮播
    """
    img = models.ImageField(upload_to='ad/', blank=False, null=False, verbose_name='广告图片')
    good = models.ForeignKey('Good')

    def __str__(self):
        return "%s的广告图片" % self.good.name

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name


class Category(models.Model):
    """
    商品分类
    """
    name = models.CharField(max_length=20, blank=False, verbose_name='商品分类')
    sex = models.SmallIntegerField(choices=((1, '男式'), (0, '女式')), null=False, default=1, blank=True, verbose_name='性别')
    # 男女式大类用sex来标识
    index = models.SmallIntegerField(default=1, blank=False, verbose_name='排序')
    # 数字小的靠前
    attrvalue = models.ManyToManyField('AttrValue', verbose_name='细节')

    def __str__(self):
        str = "男" if self.sex == 1 else "女"
        return str + "-" + self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Brand(models.Model):
    name = models.CharField(max_length=20, verbose_name='品牌')
    index = models.SmallIntegerField(default=1, verbose_name='排序')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='尺寸')
    index = models.IntegerField(default=1, verbose_name='排列顺序')

    class Meta:
        verbose_name = '尺寸'
        verbose_name_plural = verbose_name
        ordering = ['index', ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '尺寸'
        verbose_name_plural = '尺寸'


class Color(models.Model):
    name = models.CharField(max_length=10, verbose_name='颜色')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '颜色'
        verbose_name_plural = verbose_name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='标签')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Img(models.Model):
    """
    商品的图片,一个商品有多个图片
    """
    goodsku = models.ForeignKey('GoodSku', null=False)
    # good = models.ForeignKey('Good', null=False)
    url = models.ImageField('图片', upload_to='')
    # index = models.SmallIntegerField('排序')
    # uplaod_to是指定存储目录,主目录在settings.MEDIA_ROOT定义

    def __str__(self):
        return self.goodsku

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'


class Attr(models.Model):
    """
    属性列表,衣服的各种属性名称
    """
    name = models.CharField(max_length=20, verbose_name='属性名称')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '属性'
        verbose_name_plural = verbose_name
        ordering = ('name',)


class AttrValue(models.Model):
    """
    属性的值
    """
    attr = models.ForeignKey('Attr', verbose_name='属性名')
    name = models.CharField(max_length=30, verbose_name='属性值')

    def __str__(self):
        return "%s---%s" % (self.attr.name, self.name)

    class Meta:
        verbose_name = '属性值'
        verbose_name_plural = verbose_name
        ordering = ('attr__name',)  # 排序后方便选取属性


class GoodSku(models.Model):
    good = models.ForeignKey('Good', verbose_name='商品')
    artno = models.CharField(max_length=30, verbose_name='货号')
    size = models.ForeignKey(Size, verbose_name='尺寸')
    color = models.ForeignKey(Color, verbose_name='颜色')
    old_price = models.FloatField(default=0.0, verbose_name='原价')
    new_price = models.FloatField(default=0.0, verbose_name='现价')
    num = models.IntegerField(default=0, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    image = models.ImageField(upload_to='%Y%m', blank=True, null=True, verbose_name='图片')

    def cs(self):  # 计算字段要显示在修改页面中只能定义在只读字段中(否则不显示):readonly_fields = ('sc',)
        return '%s,%s' % (self.size.name, self.color.name)

    cs.short_description = '尺寸颜色'  # 用于显示时的名字 , 没有这个将显示'sc'


    def __str__(self):
        return "%s %s" % (self.size.name, self.color.name)

    def save(self, *args, **kwargs):
        """
        重写save方法,保存时更新商品的 价格,销量,库存 为sku的统计后的数据
        """
        super(self.__class__, self).save(*args, **kwargs)  # 先保存一下sku
        self.good.prices = self.good._prices()
        self.good.sales = self.good._sales()
        self.good.nums = self.good._nums()
        self.good.save()  # 更新商品的信息
    def delete(self, *args, **kwargs):
        """
        重写save方法,保存时更新商品的 价格,销量,库存 为sku的统计后的数据
        """
        super(self.__class__, self).delete(*args, **kwargs)  # 先删除sku
        self.good.prices = self.good._prices()
        self.good.sales = self.good._sales()
        self.good.nums = self.good._nums()
        self.good.save()  # 更新商品的信息

    class Meta:
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name


class Good(models.Model):
    """
    衣服
    """
    category = models.ForeignKey(Category, verbose_name='分类')
    brand = models.ForeignKey(Brand, verbose_name='品牌')
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='标签')
    name = models.CharField(max_length=100, verbose_name='名称')
    sex = models.SmallIntegerField(choices=((1, '男式'), (0, '女式')), null=False, default=1, blank=True, verbose_name='性别')
    attrvalue = models.ManyToManyField('AttrValue', verbose_name='属性')
    desc = models.CharField(max_length=200, verbose_name='简介')
    details = HTMLField(max_length=10000, verbose_name='详情')
    image = models.ImageField(upload_to='%Y%m', blank=True, null=True, verbose_name='主图')
    prices = models.CharField(max_length=20, default='0', verbose_name='价格')
    sales = models.IntegerField(default=0, verbose_name='销量')
    nums = models.IntegerField(default=0, verbose_name='库存')
    view = models.IntegerField(default=0, null=True, verbose_name='浏览量')
    def _prices(self):
        """
        价格,sku的价格区间 : '2000-2999'
        :return:
        """
        skus = self.goodsku_set.all()
        price = []
        for sku in skus:
            price.append(sku.old_price)
        price.sort()

        if price[0] == price[-1]:
            return "%s" % price[0]
        else:
            return "%s-%s" % (price[0], price[-1])

    _prices.short_description = '价格'  # 这个是计算字段 显示时的文字

    def _sales(self):
        """
        销量,sku的销量总和
        :return:
        """
        skus = self.goodsku_set.all()
        sale = 0
        for sku in skus:
            sale = sale + sku.sales
        return sale

    _sales.short_description = '销量'

    def _nums(self):
        """
        销量,sku的库存总和
        :return:
        """
        skus = self.goodsku_set.all()
        num = 0
        for sku in skus:
            num = num + sku.num
        return num

    _nums.short_description = '库存'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
        ordering = ['-view']