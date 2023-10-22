from django.shortcuts import render,redirect
from .models import Product, Costumer, Cart
from django.views import View
from .forms import RegistrationForm,CostumerForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.http import JsonResponse

class Products(View):
 def get(self, request):
  laptops = Product.objects.filter(catagory='lap')
  mobiles = Product.objects.filter(catagory='mob')

  return render(request, 'app/home.html', {"laptops": laptops, "Mobiles": mobiles})

 def __str__(self):
  return str(self.id)


######## For Product Details ############

class Product_detail(View):
 def get(self, request, pk):
  details = Product.objects.get(pk = pk)
  return render(request, 'app/productdetail.html', {"details": details})

class RegistrationFormView(View):
 def get(self, request):
  form = RegistrationForm()
  return render(request,'app/customerregistration.html', {'form': form})
 def post(self,request):
  form = RegistrationForm(request.POST)
  if form.is_valid():
   form.save()
   messages.success(request,"Registered successfully!")
  return render(request, 'app/customerregistration.html', {'form': form})

######## Login ###########

class LoginFormView(View):
 def get(self, request):
  form = AuthenticationForm()
  return render(request, 'app/login.html', {'form': form})
 def post(self, request):
  form = AuthenticationForm(request=request, data= request.POST)
  if form.is_valid():
   upass = form.cleaned_data['password']
   uname = form.cleaned_data['username']
   user = authenticate(username = uname, password =upass)
   if user is not None:
    login(request,user)
    return HttpResponseRedirect('/profile/')
   messages.success(request,"Login sucessfully")
  return render(request, 'app/login.html', {'form': form})

######## For logout #######

class Logout_user(View):
 def get(self, request):
  logout(request)
  return redirect('/login/')

######  Profile ###

class CostumerView(View):
 def get(self,request):
  form = CostumerForm()
  return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})
 def post(self,request):
  form = CostumerForm(request.POST)
  if form.is_valid():
   usr = request.user
   name = form.cleaned_data['name']
   father_name = form.cleaned_data['father_name']
   locality = form.cleaned_data['locality']
   city = form.cleaned_data['city']
   reg = Costumer(user = usr, name = name, father_name = father_name, locality= locality, city= city)
   reg.save()
  return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})


#### Address ####

def address(request):
 address = Costumer.objects.filter(user = request.user)
 return render(request, 'app/address.html', {'address':address, 'active':'btn-primary'})

#### Add TO Cart #####

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id = product_id)
 Cart(user = user, product = product).save()
 return redirect('/cart/')

def show_cart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)
  amount = 0.0
  shipping = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == user]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity * p.product.price)
    amount += tempamount
    total_amount = (amount + shipping)
   return render(request, 'app/addtocart.html', {'carts': cart,'amount': amount, 'total':total_amount})



######### for Plus button ###

def plus_button(request):
 if request.method == 'GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity += 1
  c.save()
  amount = 0.0
  shipping = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
   tempamount = (p.quantity * p.product.price)
   amount += tempamount
   total_amount = amount + shipping
  data = {
   'quantity': c.quantity,
   'amount': amount,
   'total_amount': total_amount}
  return JsonResponse(data)










# def product_detail(request):
#  return render(request, 'app/productdetail.html')



def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')



def orders(request):
 return render(request, 'app/orders.html')


def mobile(request):
 return render(request, 'app/mobile.html')

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
