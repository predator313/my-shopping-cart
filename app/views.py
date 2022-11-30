from django.shortcuts import render
from django.views import View
from .models import Customer,Product,OrderPlaced,Cart

# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobile=Product.objects.filter(category='M')
        laptop=Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobile':mobile,'laptop':laptop})



# def product_detail(request):
#  return render(request, 'app/productdetail.html')
#changing above to the class based is
class ProductDetailsView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if(data==None):
        mobile=Product.objects.filter(category='M')
    elif(data=='samsung' or data=='apple' or data=='redmi'):
        mobile=Product.objects.filter(category='M').filter(brand=data)
    elif(data=='below'):
        mobile=Product.objects.filter(category='M').filter(discount_price__lt=10000)
    elif(data=='above'):
        mobile=Product.objects.filter(category='M').filter(discount_price__gt=10000)
    return render(request, 'app/mobile.html',{'mobile':mobile})
def laptop(request,data=None):
    if(data==None):
        laptop=Product.objects.filter(category='L')
    elif(data=='acer' or data=='apple'):
        laptop=Product.objects.filter(category='L').filter(brand=data)
    elif(data=='below'):
        laptop=Product.objects.filter(category='M').filter(discount_price__lt=40000)
    elif(data=='above'):
        laptop=Product.objects.filter(category='M').filter(discount_price__gt=70000)
    return render(request, 'app/laptop.html',{'laptop':laptop})
def topwears(request,data=None):
    if(data==None):
        topwears=Product.objects.filter(category='TW')
    elif(data!=None):
        topwears=Product.objects.filter(category='TW').filter(brand=data)
    return render(request,'app/topwears.html',{'topwears':topwears})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
