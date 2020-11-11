from django.shortcuts import render
from ast import literal_eval
# Create your views here.
import pandas as pd
import time

priceList={
    'Laddu':500,
    'Pidia':300,
    'Khaja':200,
    'item4':200,
    'item5':200,
    'item6':200,
    'item7':200,
    'item8':200,
    'item9':200,
    'item10':200,
}
listOFItems={
"item1":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item2":{'name':'Pidia','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item3":{'name':'Khaja','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item4":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item5":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item6":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item7":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item8":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item9":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item10":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item11":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},
"item12":{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':500},


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

