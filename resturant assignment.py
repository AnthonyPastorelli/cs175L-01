#cs175-01
#Anthony Pastorelli
#Resturant

vegetarian='false'
vegan='false'
gluten_free='false'
response1=input('is anyone in your party a vegetarian? ')
if response1=='yes' or response1=='no':
    vegetarian='true'
response2=input('is anyone in your party a vegan? ')
if response2=='yes' or response2=='no':
    vegan='true'
response3=input('is anyone in your party gluten free? ')
if response3=='yes' or response3=='no':
    gluten_free='true'

print('\nHere are your restaurant choices: \n')

if response1=='yes':
    if response2=='yes':
        if response3=='yes' or response3=='no':
            print('corner cafe\n' +\
                  "the chef's Kitchen")
    else:
        if response3=='yes':
            print('Main street pizza company\n' + \
                  'Corner Cafe\n' + \
                  "The Chef's Kitchen\n")
        else:
            print('Main Street Pizza Company\n' + \
                  'Corner Cafe\n' + \
                  "Mama's Fine Italian\n" + \
                  "The Chef's Kitchen\n")
else:
    if response2=='yes':

        if response3=='yes' or response3=='no':
            print('corner cafe\n' + \
                  "the chef's Kitchen")
    else:
        if response3=='yes':
            print('Main Street Pizza Company\n' + \
                  'Corner Cafe\n' + \
                  "The Chef's Kitchen\n")
        else:
            print("Joe's Gourmet Burgers\n" + \
                  'Main Street Pizza Company\n' + \
                  'Corner Cafe\n' +\
                  "Mama's Fine Italian\n" + \
                  "The Chef's Kitchen\n")
            

        
      
