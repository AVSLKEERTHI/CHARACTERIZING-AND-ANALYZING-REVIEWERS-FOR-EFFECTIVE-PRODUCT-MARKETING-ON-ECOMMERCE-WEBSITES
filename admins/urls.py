from django.conf.urls import url

from admins import views

urlpattern = [
    url(r'^home/$',views.home,name='home'),
    url(r'^$',views.index,name='index'),
    url(r'^upload/products/$',views.uploadproducts,name='uploadproducts'),
    url(r'^charts/Multivendor-Analysis/(?P<chart_type>\w+)/$',views.charts,name='charts'),
    url(r'^charts/Knowledge-Based-Opinion/(?P<chart_type>\w+)/$',views.charts1,name='charts1'),
    url(r'^charts/Region-wise-Opinion-Analysis/(?P<chart_type>\w+)/$',views.charts2,name='charts2'),
    url(r'^charts/Sentiment-Wise-Analysis/(?P<chart_type>\w+)/$',views.charts3,name='charts3'),
    url(r'^logout/$',views.logout,name='logout'),
]