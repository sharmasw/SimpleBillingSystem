from django.shortcuts import render
from ast import literal_eval
import pandas as pd
import time
# Create your views here.

priceList={
    'Laddu':400,
    'Pidia':400,
    'Khaja':300,
    'Ghujia':400,
    'Papchi':300,
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
    'DawaiLaddu':700,
    'BundiLaddu':200,
    'RaitaBundi':200,
}

listOFItems=[
{'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
{'name':'Pidia','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
{'name':'Khaja','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'Ghujia','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
{'name':'Anarsa','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'Sakkarpara','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'Bidia','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'KariLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'Khurmi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'Charkoli','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'Mathri','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'Thetri','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'Namkeen','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
{'name':'Mixture1','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
{'name':'MixtureChiwda','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'Sev','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
{'name':'LaiBadi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'Bijori','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
{'name':'RakhiyaBadi','imgUrl':'./media/kol-sweet-shops.jpg','price':600},
{'name':'UradBari','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
{'name':'ChawalPapad','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
{'name':'ChawalSevMurku','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
{'name':'SabuDanaPapad','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'AlooChips','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
{'name':'DawaiLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':700},
{'name':'BundiLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
{'name':'RaitaBundi','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
{'name':'Papchi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# "item":{'name':'','imgUrl':'./media/kol-sweet-shops.jpg','price':},
# "item":{'name':'','imgUrl':'./media/kol-sweet-shops.jpg','price':},

]


def index(request):
    context={'listOFItems':listOFItems,'priceList':priceList}
    return render(request,'index.html',context)

def submitDetails(request):
    data=pd.read_csv('database.csv')
    customerNumber= request.POST.get('customerNumber')
    purchaseDetail=literal_eval(request.POST.get('purchaseDetails'))
    totalValue=request.POST.get('totalValue')

    xx =pd.DataFrame(purchaseDetail)
    xx['customerNumber']=customerNumber
    xx['transactionID']=int(time.time())
    data=pd.concat([data,xx])
    data.to_csv('database.csv',index=False)
    context={'listOFItems':listOFItems,'priceList':priceList}
    return render(request,'index.html',context)