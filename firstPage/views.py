from django.shortcuts import render
from ast import literal_eval
# Create your views here.
import pandas as pd
import time

priceList={
    'Laddu':400,
    'Pidia':400,
    'Khaja':300,
    'Ghujia':400,
    'Anarsa':300,
    'Sakkarpara':250,
    'Bidia':250,
    'KariLaddu':300,
    'Khurmi':300,
    'Charkoli':250,
    'Mathri':250,
    'Thetri':250,
    'Namkeen':200,
    'Mixture1':200,
    'MixtureChiwda':250,
    'Sev':250,
    'LaiBadi':300,
    'Bijori':400,
    'RakhiyaBadi':600,
    'UradBari':400,
    'ChawalPapad':200,
    'ChawalSevMurku':200,
    'SabuDanaPapad':300,
    'AlooChips':300,
}
listOFItems={
"item1":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
"item2":{'name':'Pidia','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
"item3":{'name':'Khaja','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
"item4":{'name':'Ghujia','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
"item5":{'name':'Anarsa','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
"item6":{'name':'Sakkarpara','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item7":{'name':'Bidia','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item8":{'name':'KariLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
"item9":{'name':'Khurmi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
"item10":{'name':'Charkoli','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item11":{'name':'Mathri','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item12":{'name':'Thetri','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item13":{'name':'Namkeen','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
"item14":{'name':'Mixture1','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
"item15":{'name':'MixtureChiwda','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item16":{'name':'Sev','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
"item17":{'name':'LaiBadi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
"item18":{'name':'Bijori','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
"item19":{'name':'RakhiyaBadi','imgUrl':'./media/kol-sweet-shops.jpg','price':600},
"item19":{'name':'UradBari','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
"item20":{'name':'ChawalPapad','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
"item21":{'name':'ChawalSevMurku','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
"item22":{'name':'SabuDanaPapad','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
"item23":{'name':'AlooChips','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# "item":{'name':'','imgUrl':'./media/kol-sweet-shops.jpg','price':},


}

def index(requests):
    contex={'listOFItems':listOFItems,"priceList":priceList}
    return render(requests,'index.html',contex)


def submitDetails(requests):
    data=pd.read_csv('database.csv')
    print (requests.POST)
    customerNumber=requests.POST.get('customerNumber')
    purchaseDetails=literal_eval(requests.POST.get('purchaseDetails'))
    # totalValue=int(requests.POST.get('totalValue'))

    xx=pd.DataFrame(purchaseDetails)
    xx['cutomerNumber']= customerNumber
    xx['transactionID']=int(time.time())

    data=pd.concat([data,xx])
    # data=data.reset_index()
    data.to_csv('database.csv',index=False)

    contex={'listOFItems':listOFItems,"priceList":priceList}
    return render(requests,'index.html',contex)


def dashboardView(requests):
    data=pd.read_csv('database.csv')
    uniqueCustomer=len(pd.unique(data['cutomerNumber']))
    uniqueTransaction=len(pd.unique(data['transactionID']))
    totalSales= sum(data['total'])
    contex={'uniqueCustomer':uniqueCustomer,"uniqueTransaction":uniqueTransaction,'totalSales':totalSales}
    return render(requests,'dashboard.html',contex)

