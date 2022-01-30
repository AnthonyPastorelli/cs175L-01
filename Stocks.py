#cs175L-01
#AnthoynPastorelli
#stocks

#input
Commission_Rate=(input('what was the commision rate?'))
Num_Shares=(input('how many shares did you purchase?'))
Purchase_Price=(input('what was the purchase price?'))
Selling_Price=(input('What was the selling price?'))
Commission_Rate= 0.03
Num_Shares= 2000
Purchase_Price= 40.0
Selling_Price= 42.75
amountPaidForStock=Num_Shares*Purchase_Price
purchaseCommission=Commission_Rate*amountPaidForStock
totalPaid=amountPaidForStock+purchaseCommission
stockSoldFor=Num_Shares*Selling_Price
sellingCommission=Commission_Rate*stockSoldFor
totalReceived=stockSoldFor-sellingCommission
profitOrLoss=totalReceived-totalPaid
print('Amount paid for Stock:',Num_Shares*Purchase_Price)
print('commission paid on the purchase:',Commission_Rate*amountPaidForStock)
print('Amount the stock sold for:',Num_Shares*Selling_Price)
print('commission paid on the sale:',Commission_Rate*stockSoldFor)
print('total commision paid:',stockSoldFor-sellingCommission)
print('Profit (or loss if negative):',totalReceived-totalPaid)


