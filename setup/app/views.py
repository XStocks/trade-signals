import asyncio
from django.contrib import messages
from django.shortcuts import redirect, render
from .stock import getData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):    
    return render(request,"index.html")

# Create your views here.
@login_required(login_url="/login")
def home(request):    
    # testHeaderData=['Sr.', 'Stock Name', 'Symbol', '% Chg', 'Price', 'Volume']
    # testStockData = [['1', 'Jindal Poly Films Limited', 'JINDALPOLY', '20%', '1090', '853,309'], ['2', 'Banco Products (i) Limited', 'BANCOINDIA', '19.99%', '151.85', '937,336'], ['3', 'Fairchem Organics Ltd', 'FAIRCHEMOR', '6.88%', '1319.65', '7,750'], ['4', 'ROUTE', 'ROUTE', '6.74%', '1193.1', '234,582'], ['5', 'Balrampur Chini Mills Limited', 'BALRAMCHIN', '6.41%', '399.5', '6,712,140'], ['6', 'Swelect Energy Systems Limited', 'SWELECTES', '4.99%', '342.9', '3,972'], ['7', 'Gulshan Polyols Limited', 'GULPOLY', '4.94%', '237.9', '45,187'], ['8', 'Kaushalya Infrastructure Development Corporation Limited', 'KAUSHALYA', '4.94%', '4.25', '37,204'], ['9', 'Kritika Wires Ltd', 'KRITIKA', '4.91%', '56.6', '57,812'], ['10', 'Standard Industries Limited', 'SIL', '4.87%', '22.6', '223,403'], ['11', 'Impex Ferro Tech Limited', 'IMPEXFERRO', '4.71%', '10', '11,647'], ['12', 'ZENITHSTL', 'ZENITHSTL', '4.61%', '7.95', '34,731'], ['13', 'Prozone Intu Properties Limited', 'PROZONINTU', '4.49%', '23.25', '95,969'], ['14', 'Ambika Cotton Mills Limited', 'AMBIKCO', '3.26%', '1847.15', '13,747'], ['15', 'Aditya Birla Sun Life AMC Ltd', 'ABSLAMC', '3.13%', '425.65', '92,795'], ['16', 'Veranda Learning Solutions Ltd', 'VERANDA', '2.76%', '197.65', '177,280'], ['17', 'Raj Rayon Industries Ltd', 'RAJRILTD', '1.74%', '8.75', '107'], ['18', 'Astral Poly Technik Limited', 'ASTRAL', '1.62%', '1689.3', '218,932']]
    # context={
    #     'headerData':testHeaderData, 
    #     'stockData':testStockData,
    # }
    [headerData, stockData]= asyncio.run(getData())
    print("headerData:- ",headerData)
    print("headerData:- ", stockData)
    context={
        'headerData':headerData, 
        'stockData':stockData,
    }
    return render(request,'stock-table.html', context)

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username= username, password=password)
        if user is not None:
            login(request, user)            
            return redirect('/home')   
        else:
            messages.error(request, "Bad Credentials","danger")
            return redirect('/login')    
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect("/login")