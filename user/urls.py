from django.conf.urls import url

from user import views

urlpattern = [
    url(r'^$',views.index,name='index'),
    url(r'^registration$',views.registration,name='registration'),
    url(r'^home/$',views.home,name='home'),
    url(r'^Cart/$',views.cart,name='cart'),
    url(r'^View/Ratings/(?P<pk>\d+)/$',views.viewratings,name='ratings'),
    url(r'^Add/Ratings/(?P<pk>\d+)/$',views.addratings,name='addratings'),
    url(r'^view/product/(?P<pk>\d+)/$',views.viewproduct,name='viewproduct'),
    url(r'^logout/$',views.logout,name='logout'),
]