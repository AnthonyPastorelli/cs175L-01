

def main():
    numbersfile=open('numbers.txt','r')
    
    total = 0
    number = 0   
    for line in numbersfile:
        number= float(line)
        total= total+number
        print(f'current numner is:     {number:.2f}     Total is: ',total)
        
    average = total/3
    print('Average: ',average)

if __name__ == "__main__":
    main()




