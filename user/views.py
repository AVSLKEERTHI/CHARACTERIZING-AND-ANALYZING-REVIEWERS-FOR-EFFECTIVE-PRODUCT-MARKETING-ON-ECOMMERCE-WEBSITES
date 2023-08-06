from django.shortcuts import render, redirect, get_object_or_404

from admins.models import Prodcuts
from user.forms import UsersForm, PurchaseForm
from user.models import Users, Purchase, Feedback
from user.words import positive_words, negative_words


def home(request):
    products=Prodcuts.objects.all()
    return render(request,'user/home.html',{'products':products})

def viewproduct(request,pk):
    pro=Prodcuts.objects.get(id=pk)
    pros=Prodcuts.objects.get(id=pk)
    uid=request.session['userid']
    uses = get_object_or_404(Users, id=uid)
    if request.method=="POST":
        form=PurchaseForm(request.POST)
        if form.is_valid():
            ff=form.save(commit=False)
            ff.customer=uses
            ff.purhased=pro
            ff.totalprice=0
            ff.save()
            return redirect('user:cart')
    else:
        form=PurchaseForm()
    return render(request,'user/viewproduct.html',{'prod':pro,'ipk':pk,'form':form})

def cart(request):
    uid = request.session['userid']
    uses = get_object_or_404(Users, id=uid)
    p=Purchase.objects.filter(customer=uses,status='incart')
    if request.method == "POST":
        Purchase.objects.filter(customer=uses, status='incart').update(status='checkout')
        return redirect('user:home')
    return render(request,'user/cart.html',{'p':p})

def viewratings(request,pk):
    pro = get_object_or_404(Prodcuts, pk=pk)
    fedbck=Feedback.objects.filter(product=pro)
    return render(request,'user/viewratings.html',{'feedbacks':fedbck})

def addratings(request,pk):
    pos,neg=0,0
    sen='pending'
    pro = get_object_or_404(Prodcuts, pk=pk)
    uid = request.session['userid']
    uses = get_object_or_404(Users, id=uid)
    stat = 'pending'
    try:
        uud = Purchase.objects.get(customer=uses,purhased=pro,status='purchased')
        stat = 'purchased'
    except:
        stat='not purchased'
    if request.method=="POST":
        ratings=request.POST.get('rating','')
        comments=request.POST.get('comment','')
        for pword in positive_words:
            if pword in comments:
                pos=pos+1
        for nword in negative_words:
            if nword in comments:
                neg=neg+1
        if pos>neg:
            sen='positive'
        elif neg>pos:
            sen='negative'
        elif neg==pos:
            sen='neutral'
        if Feedback.objects.create(user=uses,product=pro,isPurchased=stat,rating=ratings,review=comments,sentiment=sen):
            return redirect('user:home')
    return render(request,'user/addratings.html',{'pro':pro})

def index(request):
    message=None
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        try:
            users=Users.objects.get(username=username,password=password)
            request.session['userid']=users.id
            request.session['username']=users.username
            return redirect('user:home')
        except:
            message="User name and password are not matching..."
    return render(request,'user/index.html',{'msg':message})

def registration(request):
    if request.method=="POST":
        loca=request.POST.get('location','')
        users = UsersForm(request.POST)
        if users.is_valid():
            formss=users.save(commit=False)
            formss.location=loca
            formss.save()
            return redirect('user:index')
    else:
        users = UsersForm()
    return render(request,'user/registration.html',{'form':users})

def logout(request):

    return redirect('user:index')