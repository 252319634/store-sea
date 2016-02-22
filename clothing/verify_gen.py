# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import random

w = 80
h = 36
# 图片的宽高

def get_text():
    text = []
    for i in range(2):
        text.append(chr(random.randint(65, 90)))  # 大写字母
        text.append(chr(random.randint(97, 122)))  # 小写字母
    random.shuffle(text)  # 把text中的元素洗一次牌^_^!
    return ''.join(text)  # 列表转字符串


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "rgb(%d,%d,%d)" % (r, g, b)


def make_noises(drw, points=300):
    pnt = []
    for i in range(points):
        pnt.append((random.randint(5, 95), random.randint(5, 31)))
    drw.point(pnt, fill=get_color())


def get_verify():
    a = Image.new('RGB', (80, 36), 'white')
    drw = ImageDraw.Draw(a)
    myfont = ImageFont.truetype('segoeprb.ttf', size=22)
    atext = get_text()
    drw.text((10, 2), atext, font=myfont, fill='green')
    make_noises(drw)
    f = io.BytesIO()
    a.save(f, 'JPEG')
    f.seek(0)
    return f.read(), atext
# 如果运行的时候报错：
#
# IOError: cannot open resource
# 这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：
#
# '/Library/Fonts/Arial.ttf'


def verifyTheText(request):
    """
    验证request中的验证图片的信息是否正确，验证后删除requset。session中的verify.text数据
    :param request:
    :return:验证成功返回True，否则返回False
    """
    checkCode = request.POST.get("verify_text", '').strip().lower()  # 表单中的验证码
    theCheckCode = request.session.get('verify_text', '').strip().lower()
    if theCheckCode:
        del request.session['verify_text']  # 取出后删除session中的'verify_text'
    # 正确的验证码,verify()方法中,生成的时候存进session中了 .
    # print('checkCode:',checkCode)
    # print('thecheckCode:',theCheckCode)
    if checkCode == theCheckCode:
        return True
    return False