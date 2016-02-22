# coding=utf-8
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AnonymousUser, User
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from clothing import forms
from clothing.searchtools import add_to_session
from clothing.verify_gen import get_verify, verifyTheText
from models import *
from store import settings
import logging

logger = logging.getLogger('store.views')


def verify(request):
    """
    生成验证码图片
    :param request:
    :return:
    # 返回的内容是图片要用 content_type='image/jpge' 来说明.不能直接return img
    """
    img, text = get_verify()
    request.session['verify_text'] = text
    return HttpResponse(img, content_type='image/jpeg')


def global_setting(request):
    setting = settings  # 设置参数,主要用到(店名,是否开启验证码)
    MEDIA_URL = settings.MEDIA_URL  # 媒体路径
    ADS = Ad.objects.all()  # 广告
    CATEGORY = Category.objects.all()  # 分类信息
    GOOD_MAN = Good.objects.filter(sex=1)  # 所有男式商品
    # BRAND_MAN = Brand.objects.filter(sex=1).values('id', 'name').distinct()  # 男式品牌
    BRAND_MAN = Brand.objects.filter(good__sex=1).distinct()[:10]  # distinct去重 所有的男式品牌
    BRAND_WOMAN = Brand.objects.filter(good__sex=0).distinct()[:10]  # distinct去重  # 女式品牌
    NEW = Good.objects.all().order_by('-pk')[:4]  # 最新商品
    HOT = Good.objects.all().order_by('-sales')[:4]  # 最新商品
    TAG = Tag.objects.all()  # 标签

    return locals()


def getPage(request, list1, num=8):
    """
    返回了一个page对象,给list1加上了一些分页相关的属性,默认8个商品一页
    """
    paginator = Paginator(list1, num)
    try:
        page = int(request.GET.get('page', 1))
        list1 = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        list1 = paginator.page(1)
    return list1


def index(request):
    # g = global_setting(request)
    g_list = Good.objects.all()
    g_list = getPage(request, g_list)
    return render(request, "index.html", locals())  # 这个可以使用上下文管理器中的变量.
    # return render_to_response('index.html', locals(), context_instance=RequestContext(request))  # 这个方法也可以正常使用
    # return render_to_response('index.html', locals()) 这个方法不能正常使用,因为不能用到上下文管理器中的变量.


def mylogin(request):
    user = get_user(request)
    # 先取出 session 中的已登录的用户的 userid, backend 信息，
    # 然后根据 backend 路径加载相关 backend 模块，
    # 调用 backend 的 get_user 方法获取用户。
    # 以上流程如果失败，则返回一个 AnonymousUser.
    is_verify = settings.VERIFY
    if user.is_anonymous():
        print(user)
        print('匿名用户')
        try:
            if request.method == "POST":
                login_form = forms.LoginForm(request.POST)  # 获得一个form对象,传入POST的参数
                if is_verify:
                    if not verifyTheText(request):
                        verifyError = "验证码错误"
                        return render(request, 'login.html', locals())
                if login_form.is_valid():
                    # 验证表单数据,is_valid()方法验证所有的字段,如果都合法则返回True,并把验证后的数据放在cleaned_data属性中.
                    # 如果验证失败,返回False,并把验证的错误信息保存在errors属性中.
                    username = login_form.cleaned_data["username"]  # 从cleaned_data中获得username
                    password = login_form.cleaned_data["password"]  # 从cleaned_data中获得password
                    user = authenticate(username=username, password=password)
                    # 对指定的用户名/密码或其他身份凭据（用 kwargs 方式指定的，因此可扩展）进行验证，
                    # 成功返回 user，失败返回 None.
                    # 如果验证成功，authenticate 方法还会给返回的 user 对象添加 backend 属性，指示是哪个配置的后台代码验证成功。
                    if user:
                        login(request, user)
                        # 向 session 中添加 user.id, user.backend 两个值
                        url = request.POST.get('source_url')
                        if 'register/' in url:
                            url = '/'
                        if not url:
                            url = '/'
                        return redirect(url)
                    else:
                        login_form.errors["message"] = "用户名或密码错误!"
                        return render(request, "login.html", locals())
                else:
                    return render(request, 'login.html', locals())
            else:
                login_form = forms.LoginForm()
                return render(request, 'login.html', locals())
        except Exception as e:
            pass
    else:  # 如果不是匿名用户就跳转到原网址
        print(user)
        # url = request.POST.get('source_url')
        # if not url:
        # url = '/'
        return render(request, 'login.html', locals())


def mylogout(request):
    try:
        logout(request)
    except Exception as e:
        pass
        # logger.error(e)
    url = request.META.get('HTTP_REFERER', '/')
    return redirect(url)


def myregister(request):
    is_verify = settings.VERIFY
    try:
        if request.method == "POST":
            reg_form = forms.RegisterForm(request.POST)
            if is_verify:
                if not verifyTheText(request):
                    verifyError = "验证码错误"
                    return render(request, 'register.html', locals())
            if reg_form.is_valid():
                username = reg_form.cleaned_data['username']
                password = reg_form.cleaned_data['password']
                email = reg_form.cleaned_data['email']
                # 验证用户名邮箱是否被使用,验证放在了表单字段验证方法里了.
                # user = User.objects.filter(username=username)
                # if user:
                # reg_form.errors['message'] = '用户名已存在'
                # return render(request, "register.html", locals())
                # user = User.objects.filter(email=email)
                # if user:
                # reg_form.errors['message'] = '邮箱已被使用'
                # return render(request, "register.html", locals())
                user = User.objects.create_user(username=username, password=make_password(password), email=email)
                user.save()
                userprofile = UserProfile(user=user)
                userprofile.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                # 如果没有backend 报错:'User' object has no attribute 'backend'
                login(request, user)  # login()必须要求user对象有一个banckend属性
                return redirect('/')
            else:
                return render(request, "register.html", locals())
        else:
            reg_form = forms.RegisterForm()

    except Exception, e:
        pass
    return render(request, "register.html", locals())


def search(request):
    # g = global_setting(request)

    g = Good.objects.all()

    def attrname(name):
        itemlist = {"category": Category, "brand": Brand, "tag": Tag}
        item = itemlist[name]
        return item

    # 已选条件 及 筛选出的商品↓

    # 设置筛选关键字
    keys = request.GET.get('search_keys', '')  # 得到关键字
    if keys == "-":  # 如果关键字是"-"
        request.session['search_keys'] = ""  # 把session中的关键字设置为空
    elif keys:
        request.session['search_keys'] = keys
        # 关键字不是"-",就把关键字设置为获得的关键字,这样可以实现主动设置关键字的有无,不会因为url中没有keys参数就被设置为空

    # 设置选项
    act = request.GET.get('act', '')
    if act == "add":  # 增加选项
        item = request.GET.get('item', '')
        id = request.GET.get('id', '')
        name = str(attrname(item).objects.get(id=id))
        add_to_session(request, item, id, name)  # 把选项的item,name,id添加到session.
        # 如:item:"category",id:1, name:"女---T恤&POLO衫"
    elif act == "sub":  # 减少选项
        item = request.GET.get('item', '')
        try:
            del request.session[item]  # 删除这个选项
        except Exception:
            pass
    # 根据关键字筛选商品
    try:
        if request.session['search_keys']:
            keys = request.session['search_keys']
            onekeys = keys.split(' ')
            for k in onekeys:
                g = g.filter(name__icontains=k)  # 过滤商品为含有关键字的商品
    except Exception as e:
        logger.error(e)

    # 根据category筛选商品
    item = request.session.get("category", '')
    if item:
        id = int(item.get('id'))
        category = Category.objects.get(id=id)  # 这个用于显示到页面中的已选条件
        g = g.filter(category=category)
    else:
        category = Category.objects.all()  # 显示到页面中的可选条件
    # 根据brand筛选商品
    item = request.session.get("brand", '')
    if item:
        id = int(item.get('id'))
        brand = Brand.objects.get(id=id)
        g = g.filter(brand=brand)
    else:
        brand = Brand.objects.all()
    # 根据tag筛选商品
    item = request.session.get("tag", '')
    if item:
        id = int(item.get('id'))
        tag = Tag.objects.get(id=id)
        g = g.filter(tag=tag)
    else:
        tag = Tag.objects.all()

    g_list = getPage(request, g, num=20)
    # 已选条件 及 筛选出的商品↑
    return render(request, "search.html", locals())


def man(request):
    # g = global_setting(request)
    t = '所有男装'
    g_list = Good.objects.filter(sex=1)
    g_list = getPage(request, g_list)
    return render(request, "special.html", locals())


def woman(request):
    t = '所有女装'
    g_list = Good.objects.filter(sex=0)
    g_list = getPage(request, g_list)
    return render(request, "special.html", locals())


def brand(request):
    try:
        bid = request.GET.get('bid', None)
        try:
            b = Brand.objects.get(pk=bid)
            t = b.name
        except Brand.DoesNotExist:
            return render(request, 'error.html', {"reason": "品牌不存在"})
    except Exception as e:
        print e
        # logger.error(e)
    g_list = Good.objects.filter(brand=b)
    g_list = getPage(request, g_list)
    return render(request, "special.html", locals())


def category(request):
    try:
        cid = request.GET.get('cid', None)
        try:
            c = Category.objects.get(pk=cid)
            t = c.name
        except Brand.DoesNotExist:
            return render(request, 'error.html', {"reason": "分类不存在"})
    except Exception as e:
        print e
        # logger.error(e)
    g_list = Good.objects.filter(category=c)
    g_list = getPage(request, g_list)
    return render(request, "special.html", locals())


def products(request):
    # 得到商品id
    try:
        pid = request.GET.get('pid', None)
        user = get_user(request)
        if user.is_anonymous():
            pass
        else:
            pass
            userprofile = UserProfile.objects.get(user=user)
            view_history = userprofile.view_history.split(',')
            if '' in view_history:
                view_history.remove('')
            if str(pid) not in view_history:
                view_history.append(str(pid))
                if len(view_history)>6:
                    view_history = view_history[-6:]
                userprofile.view_history = ','.join(view_history)
                userprofile.view_history.strip(',')
                userprofile.save()
            else:
                view_history.remove(str(pid))
                view_history.append(str(pid))
                if len(view_history)>6:
                    view_history = view_history[-6:-1]
                userprofile.view_history = ','.join(view_history)
                userprofile.save()
        try:
            p = Good.objects.get(pk=pid)  # 查询到商品对象
            p.view += 1
            p.save()

        except Good.DoesNotExist:
            return render(request, 'error.html', {"reason": "商品不存在"})
    except Exception as e:
        print e
        # logger.error(e)

    return render(request, 'product.html', locals())


@login_required(login_url='/login/')  # 需要登录
def mycart(request):
    # 购物车,删除物品,增加减少物品数量,设置结算否

    if request.method == 'POST':
        skuid = request.POST.get('sku_id')
        num = request.POST.get('num')
        goodsku = GoodSku.objects.get(id=skuid)
        cart = Cart.objects.filter(user=request.user, goodsku=goodsku)
        if not cart:
            cart = Cart(user=request.user, goodsku=goodsku, count=num)
            if cart.count > goodsku.num:
                cart.count = cart.goodsku.num
            cart.save()
        else:
            cart[0].count += int(num)
            if cart[0].count > cart[0].goodsku.num:
                cart[0].count = cart[0].goodsku.num
            cart[0].save()
        return redirect('/cart/')

    try:
        # 减少物品数量
        if request.GET.get('act', '') == 'sub':
            cartid = request.GET.get('cartid')
            cart = Cart.objects.get(id=cartid)
            if cart.count > 1:
                cart.count -= 1
                cart.save()
        # 增加物品数量
        if request.GET.get('act', '') == 'add':
            cartid = request.GET.get('cartid')
            cart = Cart.objects.get(id=cartid)
            goodsku_num = cart.goodsku.num  # 得到库存
            if cart.count < goodsku_num:
                cart.count += 1
                cart.save()
        # 设置物品为结算
        if request.GET.get('act', '') == 'False':
            cartid = request.GET.get('cartid')
            cart = Cart.objects.get(id=cartid)
            cart.selected = True
            cart.save()
        # 设置物品为不结算
        if request.GET.get('act', '') == 'True':
            cartid = request.GET.get('cartid')
            cart = Cart.objects.get(id=cartid)
            cart.selected = False
            cart.save()
        # 删除物品
        if request.GET.get('act', '') == 'del':
            cartid = request.GET.get('cartid')
            cart = Cart.objects.get(id=cartid)
            cart.delete()
            # 添加物品

    except Exception as e:
        print Exception, e
    cart = Cart.objects.filter(user=request.user)
    # cart_json = serializers.serialize('json', cart)
    cart.total_price = 0
    for i in cart:
        if i.selected:  # 计算被选中的商品总价
            cart.total_price += i.sum_price()
    return render(request, 'cart.html', locals())


@login_required(login_url='/login/')  # 需要登录
def mycheckout(request):
    user = get_user(request)
    userprofile = UserProfile.objects.get(user=user)
    cart = Cart.objects.filter(user=user, selected=True)
    if request.method == 'GET':
        cart.total_price = 0
        for i in cart:
            cart.total_price += i.sum_price()
        return render(request, 'checkout_view.html', locals())
    if request.method == 'POST':
        if cart:
            now = datetime.datetime.now()
            orderid = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(
                now.second) + "u%s" % (user.pk)
            address = "%s %s %s" % (userprofile.recipients, userprofile.tel, userprofile.address)
            order = Order(user=user, orderid=orderid, time=now, address=address)
            order.save()
            for i in cart:
                selling = Selling(order=order, goodsku=i.goodsku, count=i.count, price=i.goodsku.new_price)
                selling.save()  # 保存在销售记录里
                goodsku = GoodSku.objects.get(id=i.goodsku.pk)
                goodsku.sales += i.count  # 更新sku的销量
                goodsku.num -= i.count  # 更新sku的库存数量
                goodsku.save()
                i.delete()  # 从购物车中删除
            return render(request, 'checkout_message.html', locals())
        else:
            return redirect('/cart/')


# 用户后台,管理地址,浏览记录,购买记录
@login_required(login_url='/login/')  # 需要登录
def myuser(request):
    user = get_user(request)
    if request.method == 'GET':
        userprofile = UserProfile.objects.get(user=user)
        # 获得浏览记录
        view_history = [int(x) for x in userprofile.view_history.split(',')]
        view_history.reverse()
        addressform = forms.AddressForm(instance=userprofile)
        order = Order.objects.filter(user=user)
        selling = Selling.objects.filter(order=order)
        g_list = getPage(request, order, 5)
        return render(request, 'user.html', locals())

    if request.method == 'POST':
        # 更新收货地址
        addressform = forms.AddressForm(request.POST)
        if addressform.is_valid():
            recipients = addressform.cleaned_data['recipients']
            qq = addressform.cleaned_data['qq']
            tel = addressform.cleaned_data['tel']
            address = addressform.cleaned_data['address']
            userprofile = UserProfile.objects.get(user=user)
            userprofile.recipients = recipients
            userprofile.qq = qq
            userprofile.tel = tel
            userprofile.address = address
            userprofile.save()
        return redirect('/user/')