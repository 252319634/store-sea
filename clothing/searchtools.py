# -*- coding: utf-8 -*-

def add_to_session(request, item, id, name):
    request.session[item] = {"name": name, "id": id}
    # request.session[item] = id
    # 加入session,注意db模式要使用字典，不能直接使用对象