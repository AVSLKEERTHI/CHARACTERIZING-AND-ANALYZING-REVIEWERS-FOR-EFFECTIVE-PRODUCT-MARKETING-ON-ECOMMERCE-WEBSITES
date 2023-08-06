from django.db.models import Count, Avg
from django.shortcuts import render, redirect, get_object_or_404

from admins.forms import UploadForm
from admins.models import Prodcuts
from user.models import Purchase, Feedback


def index(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='admin' and password=='admin':
            request.session['userid']=1
            request.session['username']='admin'
            return redirect('admins:home')
    return render(request,'admins/index.html',)

def home(request):
    products=Prodcuts.objects.all()
    return render(request,'admins/home.html',{'products':products})

def uploadproducts(request):
    if request.method=="POST":
        forms=UploadForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('admins:home')
    else:
        forms = UploadForm()
    return render(request,'admins/uploadproducts.html',{'form':forms})

def charts(request,chart_type):
    d=None
    if chart_type=='all':
        d=Feedback.objects.values('product').annotate(dcount=Count('rating'))
    elif chart_type=='mobile':
        d = Feedback.objects.filter(product__product_name='mobile').values('product__vendor_name').annotate(dcount=Count('rating'))
    elif chart_type=='laptop':
        d = Feedback.objects.filter(product__product_name='laptop').values('product__vendor_name').annotate(
            dcount=Count('rating'))
    elif chart_type=='mobileaccessories':
        d = Feedback.objects.filter(product__product_name='mobile accessories').values('product__vendor_name').annotate(
            dcount=Count('rating'))
    elif chart_type=='watches':
        d = Feedback.objects.filter(product__product_name='watches').values('product__vendor_name').annotate(
            dcount=Count('rating'))
    elif chart_type=='shoes':
        d = Feedback.objects.filter(product__product_name='shoes').values('product__vendor_name').annotate(
            dcount=Count('rating'))
    return render(request,'admins/charts.html',{'chart_type':chart_type,'d':d})

def charts1(request,chart_type):
    d = Feedback.objects.values('user__profession').annotate(dcount=Count('rating'))
    return render(request,'admins/charts1.html',{'chart_type':chart_type,'d':d})

def charts2(request,chart_type):
    d=Feedback.objects.values('user__location').annotate(dcount=Count('rating'))
    return render(request,'admins/charts2.html',{'chart_type':chart_type,'d':d})
    
def charts3(request,chart_type):
    d1=Feedback.objects.filter(sentiment='positive').values('product__product_name').annotate(dcount=Count('sentiment'))
    d2=Feedback.objects.filter(sentiment='negative').values('product__product_name').annotate(dcount=Count('sentiment'))
    return render(request,'admins/charts3.html',{'chart_type':chart_type,'d1':d1,'d2':d2})

def logout(request):

    return redirect('admins:index')