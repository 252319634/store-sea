# coding: utf-8

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from store import settings
from clothing import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^verify/', views.verify),  # 这个没有$,后面要加随机数字
    url(r'^user/$', views.myuser, name='user'),
    url(r'^login/$', views.mylogin, name='login'),
    url(r'^logout/$', views.mylogout, name='logout'),
    url(r'^register/$', views.myregister, name='register'),
    url(r'^cart/$', views.mycart, name='cart'),
    url(r'^checkout/$', views.mycheckout, name='checkout'),
    # name参数在模板中的用法:{% url 'index' %} -> href="/"
    # url(r'^products/$', views.products, name='products'),
    url(r'^product/$', views.products, name='product'),
    # 带参数的url在模板中的写法:{% url 'products' n.id %}(n.id=1) -> href="/products/1"
    url(r'^brand/$', views.brand, name='brand'),
    url(r'^category/$', views.category, name='category'),
    url(r'^search/$', views.search, name='search'),
    url(r'^man/$', views.man, name='man'),
    url(r'^woman/$', views.woman, name='woman'),
    url(r'^tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)