# -*- coding: utf-8 -*-
from django import template
from store import settings
import datetime
from clothing.models import *

register = template.Library()


@register.filter()
def price(id):
    """
    返回商品的第一个sku的价格
    """
    try:
        p = GoodSku.objects.filter(good_id=id)[0]
    except Exception:
        return 0
    return p.new_price


@register.filter()
def size(p):
    """
    返回商品的所有sku的尺寸
    参数是一个商品对象
    """
    sizelist = []
    sizestr = ''
    for sku in p.goodsku_set.all():
        if not sku.size.name in sizelist:
            sizelist.append(sku.size.name)

    for s in sizelist:
        sizestr += '<li>%s</li>' % s

    return sizestr


@register.filter()
def color(p):
    """
    返回商品的所有sku的尺寸
    参数是一个商品对象
    """
    colorlist = []
    colorstr = ''
    for sku in p.goodsku_set.all():
        if not sku.color.name in colorlist:
            colorlist.append(sku.color.name)

    for s in colorlist:
        colorstr += '<li>%s</li>' % s

    return colorstr


@register.inclusion_tag('include/product_block.html')
def product(p):
    """
    包含标签用来输出单个商品的展示块(主图,商品名,价格,销量)
    """
    MEDIA_URL = settings.MEDIA_URL
    try:
        p = Good.objects.get(id=p)
    except Exception:
        pass
    return {'p': p, 'MEDIA_URL': MEDIA_URL}
@register.inclusion_tag('include/history_block.html')
def history(pid):
    """
    包含标签用来输出单个商品的展示块(主图,商品名,价格,销量)
    """
    MEDIA_URL = settings.MEDIA_URL
    try:
        p = Good.objects.get(id=pid)
    except Exception:
        pass
    return {'p': p, 'MEDIA_URL': MEDIA_URL}

# @register.inclusion_tag('include/product_detail.html')
# def product_detail(p):
# """
#     包含标签用来输出单个商品图片框
#     加入购物车及选项
#     """
#     MEDIA_URL = settings.MEDIA_URL
#     return {'p': p, 'MEDIA_URL': MEDIA_URL}



