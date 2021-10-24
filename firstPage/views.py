from django.shortcuts import render
from ast import literal_eval
import pandas as pd
import time,datetime
from django.http import JsonResponse
# Create your views here.


listOFItems1= pd.read_csv('itemDetails.csv')
listOFItems= [{'name':listOFItems1['name'][i],'price':listOFItems1['price'][i]} for i in range(listOFItems1.shape[0])]
priceList={}
for i in range(listOFItems1.shape[0]):
    priceList[listOFItems1['name'][i]]=listOFItems1['price'][i]

# {'name':'Laddu','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
# {'name':'Pidia','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
# {'name':'Khaja','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'Ghujia','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
# {'name':'Anarsa','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'Sakkarpara','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'Bidia','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'KariLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'Khurmi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'Charkoli','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'Mathri','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'Thetri','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'Namkeen','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
# {'name':'Mixture1','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
# {'name':'MixtureChiwda','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'Sev','imgUrl':'./media/kol-sweet-shops.jpg','price':250},
# {'name':'LaiBadi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'Bijori','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
# {'name':'RakhiyaBadi','imgUrl':'./media/kol-sweet-shops.jpg','price':600},
# {'name':'UradBari','imgUrl':'./media/kol-sweet-shops.jpg','price':400},
# {'name':'ChawalPapad','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
# {'name':'ChawalSevMurku','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
# {'name':'SabuDanaPapad','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'AlooChips','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# {'name':'DawaiLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':700},
# {'name':'BundiLaddu','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
# {'name':'RaitaBundi','imgUrl':'./media/kol-sweet-shops.jpg','price':200},
# {'name':'Papchi','imgUrl':'./media/kol-sweet-shops.jpg','price':300},
# # "item":{'name':'','imgUrl':'./media/kol-sweet-shops.jpg','price':},
# # "item":{'name':'','imgUrl':'./media/kol-sweet-shops.jpg','price':},

# ]


from firstPage.models import BillingDetail,TimeStampDetails

def index(request):
    # print (priceList)
    context={'listOFItems':listOFItems,'priceList':priceList}
    return render(request,'index.html',context)

def submitDetails(request):
    # data=pd.read_csv('database.csv')
    customerNumber= request.POST.get('customerNumber')
    purchaseDetail=literal_eval(request.POST.get('purchaseDetails'))
    # timeStamp=request.POST.get('timeStamp')  
    timeStamp=time.time()
    transactionID=int(timeStamp)
    # timeStamp=int(timeStamp)  #Only for quick upload data
    timeStamp=datetime.datetime.fromtimestamp(timeStamp)

    for i in purchaseDetail:
        p = BillingDetail(customerNumber=customerNumber,transactionID=transactionID,timestamp=timeStamp,
        name=i['name'],quantity=i['quantity'],price=i['price'],total=i['total'],)
        p.save()

    transaction_date=timeStamp.date()
    transaction_year=timeStamp.year
    transaction_month=timeStamp.month
    transaction_day=timeStamp.day
    transaction_hour=timeStamp.hour
    transaction_minute=timeStamp.minute
    transaction_week=timeStamp.isocalendar()[1]
    transaction_weekNum=timeStamp.isocalendar()[2]

    k = TimeStampDetails(transactionID=transactionID,transaction_date=transaction_date,
    transaction_year = transaction_year,transaction_month=transaction_month,
    transaction_day=transaction_day,transaction_hour=transaction_hour,
    transaction_minute=transaction_minute,transaction_week=transaction_week,
    transaction_weekNum=transaction_weekNum)

    k.save()
         
    context={'listOFItems':listOFItems,'priceList':priceList}
    return render(request,'index.html',context)

# def submitDetails(request):
#     data=pd.read_csv('database.csv')
#     customerNumber= request.POST.get('customerNumber')
#     purchaseDetail=literal_eval(request.POST.get('purchaseDetails'))
#     totalValue=request.POST.get('totalValue')

#     xx =pd.DataFrame(purchaseDetail)
#     xx['customerNumber']=customerNumber
#     xx['transactionID']=int(time.time())
#     data=pd.concat([data,xx])
#     data.to_csv('database.csv',index=False)
#     context={'listOFItems':listOFItems,'priceList':priceList}
#     return render(request,'index.html',context)


def dashboardView(request):
    p = BillingDetail.objects.all()
    q= TimeStampDetails.objects.all()
    t1=[]
    for i in p:
        t1.append({'customerNumber':i.customerNumber,'transactionID':i.transactionID,'timestamp':i.timestamp,'name':i.name,'quantity':i.quantity,'price':i.price,'total':i.total})

    t1=pd.DataFrame(t1)
    # print (t1)

    t2=[]
    for i in q:
        t2.append({'transactionID':i.transactionID,'transaction_date':i.transaction_date,'transaction_year':i.transaction_year,'transaction_month':i.transaction_month,
        'transaction_day':i.transaction_day,'transaction_hour':i.transaction_hour,'transaction_minute':i.transaction_minute,'transaction_week':i.transaction_week,'transaction_weekNum':i.transaction_weekNum})

    t2=pd.DataFrame(t2)
    print (t2.shape,t1.shape)

    data=pd.merge(t1,t2,on='transactionID',how='left')
    totalNumberOfUniqueCustomer=len(pd.unique(data['customerNumber']))
    totalNumberOfUniqueTransaction=len(pd.unique(data['transactionID']))
    last7dayTransaction=data.groupby('transaction_date').agg({'total':'sum'}).reset_index().tail(7)
    last7dayTranscationDates,last7dayTranscationTotals=last7dayTransaction['transaction_date'],last7dayTransaction['total']
    last7dayTranscationDates=[str(i) for i in last7dayTranscationDates]
    last7dayTranscationTotals=[int(i) for i in last7dayTranscationTotals]
    last20Transaction=data.groupby('transactionID').agg({'total':'sum'}).reset_index().tail(20)
    last20TransactionDates,last20TransactionTotals=last20Transaction['transactionID'],last20Transaction['total']
    last20TransactionTotals=[int(i) for i in last20TransactionTotals]
    context={'totalNumberOfUniqueCustomer':totalNumberOfUniqueCustomer,'totalNumberOfUniqueTransaction':totalNumberOfUniqueTransaction,
            'last7dayTranscationDates':last7dayTranscationDates,'last7dayTranscationTotals':last7dayTranscationTotals,
            'last20TransactionDates':last20TransactionDates.tolist(),'last20TransactionTotals':last20TransactionTotals}
    return render(request,'dashboard.html',context)

def takeDump(request):
     p = BillingDetail.objects.all()
     listofNumbers=[]
     for i in p:
         listofNumbers.append(i.customerNumber)
     return JsonResponse({'a':listofNumbers})