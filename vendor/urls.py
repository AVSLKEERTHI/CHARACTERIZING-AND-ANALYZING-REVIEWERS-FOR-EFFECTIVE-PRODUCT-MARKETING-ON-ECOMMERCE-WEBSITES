from django.conf.urls import url

from vendor import views

urlpattern = [
    url(r'^$',views.home,name='home'),
]