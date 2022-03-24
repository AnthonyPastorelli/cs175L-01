

def main():
    numbersfile=open('numbers.txt','r')
    
    total = 0.0
    number = 0
    count=0
    for line in numbersfile:
        number= float(line)
        count+= 1
        total= total+number
        print(f'current numner is:     {number:.2f}     Total is: ',total)
        
    average = total/count
    print('Average: ',average)

if __name__ == "__main__":
    main()




