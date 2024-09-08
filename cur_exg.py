import requests as rq
curl='https://api.coinbase.com/v2/exchange-rates'
stockdata=[
    {
     'stockname':'sbi',
     'price':782.50,
     'currency':'INR',
     },
     {
       'stockname':'lic',
       'price':1038.90,
       'currency':'INR',

     },
     {
        'stockname':'google',
        'price':163.38,
        'currency':'USD'
     },

]

def getcurrencyrates(price,currency):
    queryparams={
        'currency':'INR'
    }
    cresp=rq.get(url=curl,params=queryparams)
    print(cresp.status_code)

    if currency=='INR':

        USDrate=float(cresp.json()['data']['rates']['USD'])
        print(f'newrate={USDrate*price}')
        return USDrate*price
    else:
        INRrate=float(cresp.json()['data']['rates']['INR'])
        print(f'newrate={INRrate*price}')
        return INRrate*price
     
     
newstocklist=[]

for stock in stockdata:
    print(stock['currency'])
    newcurrencyrate=getcurrencyrates(stock['price'],stock['currency'])
    stock['exchangerate']=newcurrencyrate
    newstocklist.append(stock)

print()
print(newstocklist)
print()



