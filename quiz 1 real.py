#cs175
#Anthony Pastorelli
# Rainfall.py


total=0
month=0
average=0
num_of_years=int(input( 'enter number of years(1 to 3): '))
while num_of_years<1 or num_of_years>3:
    print('error must be in range from 1 to 3')
    num_of_years=int(input( 'enter number of years(1 to 3): '))
for x in range(1,num_of_years+1):
    print('for year',x,':')
    for x in range(1,12+1):
        month=float(input('enter the rainfall amount for the month: '))
        total=month+total
print('for',x*num_of_years,'months')
print('total rainfall: ',total,'inches')
print('average mounthly rainfall: ',f'{total/(x*num_of_years):.2f}','inches')
            
            
