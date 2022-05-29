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
    # testHeaderData=['Sr.', 'Stock Name', 'Symbol', 'Links', '% Chg', 'Price', 'Volume']
    # testStockData = [['1', 'Dr. Lal Path Labs Ltd.', 'LALPATHLAB', 'P&F | F.A', '9.67%', '2204.5'], ['2', 'INDIAMART', 'INDIAMART', 'P&F | F.A', '8.16%', '4515.3'], ['3', 'Mahindra Cie Automotive Limited', 'MAHINDCIE', 'P&F | F.A', '7.03%', '188.8'], ['4', 'ROUTE', 'ROUTE', 'P&F | F.A', '6.74%', '1193.1'], ['5', 'Balrampur Chini Mills Limited', 'BALRAMCHIN', 'P&F | F.A', '6.41%', '399.5'], ['6', 'Uflex Limited', 'UFLEX', 'P&F | F.A', '6.38%', '596.3'], ['7', 'Coforge (Niit Tech)', 'COFORGE', 'P&F | F.A', '5.57%', '3671.45'], ['8', 'Eid Parry India Limited', 'EIDPARRY', 'P&F | F.A', '5.33%', '528.8'], ['9', 'Jubilant Ingrevia Ltd', 'JUBLINGREA', 'P&F | F.A', '5.12%', '468.85'], ['10', 'Poonawalla Fincorp Ltd', 'POONAWALLA', 'P&F | F.A', '4.93%', '244.9'], ['11', 'Kei Industries Limited', 'KEI', 'P&F | F.A', '4.88%', '1205.05'], ['12', 'Firstsource Solutions Limited', 'FSL', 'P&F | F.A', '4.66%', '107.7'], ['13', 'Tata Steel Long Products Ltd', 'TATASTLLP', 'P&F | F.A', '4.64%', '663.15'], ['14', 'Cyient Limited', 'CYIENT', 'P&F | F.A', '3.86%', '780.8'], ['15', 'Tata Communications Limited', 'TATACOMM', 'P&F | F.A', '3.78%', '979.25'], ['16', 'Finolex Industries Limited', 'FINPIPE', 'P&F | F.A', '3.66%', '144.4'], ['17', 'Zee Entertainment Enterprises Limited', 'ZEEL', 'P&F | F.A', '3.31%', '237.4'], ['18', 'Larsen & Toubro Infotech Limited', 'LTI', 'P&F | F.A', '3.19%', '3998'], ['19', 'Aditya Birla Sun Life AMC Ltd', 'ABSLAMC', 'P&F | F.A', '3.13%', '425.65'], ['20', 'Indusind Bank Limited', 'INDUSINDBK', 'P&F | F.A', '3.1%', '925.4'], ['21', 'Wipro Limited', 'WIPRO', 'P&F | F.A', '3%', '466.95'], ['22', 'Indian Overseas Bank', 'IOB', 'P&F | F.A', '2.65%', '17.45'], ['23', 'Infosys Limited', 'INFY', 'P&F | F.A', '2.63%', '1461.35'], ['24', 'Trident Limited', 'TRIDENT', 'P&F | F.A', '2.58%', '45.8'], ['25', 'Hcl Technologies Limited', 'HCLTECH', 'P&F | F.A', '2.37%', '1003.9']]
    # context={
    #     'headerData':testHeaderData, 
    #     'stockData':testStockData,
    # }
    [headerData, stockData]= asyncio.run(getData())
    # print("headerData:- ",headerData)
    # print("headerData:- ", stockData)
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