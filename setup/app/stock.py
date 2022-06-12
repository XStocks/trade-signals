from pyppeteer import launch
from requests_html import AsyncHTMLSession
import time
#create the session
import environ
env = environ.Env()
environ.Env.read_env()
async def getData():
    URL = 'https://chartink.com/screener/rsi-above-80-in-5-min-time-frame'
    session = AsyncHTMLSession()   
    mode = env('MODE')
    if mode == "DEV":
        browser = await launch({        
            'ignoreHTTPSErrors': True,
            'headless': True,
            'handleSIGINT': False,
            'handleSIGTERM': False,
            'handleSIGHUP': False
        })     

    if mode == "PROD":
        browser = await launch(
            headless=True, 
            ignoreHTTPSErrors=True,
            executablePath='/usr/bin/google-chrome-stable',
            args=[
                '--no-sandbox',
                '--single-process',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--no-zygote'
            ])
    session._browser = browser    
    start = time.time()
    r =await session.get(URL)
    await r.html.arender(timeout=60)
    await session.close()

    headerData = [] 
    stocksData = []

    stocks = r.html.find('#DataTables_Table_0',first=True)

    i=0
    flag=True
    d=[]
    if stocks.text:
        for t in stocks.text.split("\n"):
            if flag == True:
                # Removing links
                if i!=3:  
                    headerData.append(t)
                if i == 6:
                    i=-1
                    flag=False                
            else:
                if i<=6:
                    if i!=3:
                        d.append(t)                                         
                else:
                    stocksData.append(d)
                    d=[]    
                    if i!=3:                
                        d.append(t)
                    i=0
            i+=1

    # print("headerData:- ",headerData)
    # print("headerData:- ", stocksData)

    end = time.time()
    print("Execution Time in sec ", end - start)
    return [headerData, stocksData]
