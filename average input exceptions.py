def main():
    try:
        numbersfile=open('numbers.txt','r')
    except IOError:
        print('An error occurred trying to read the file.')
        sys.exit()
    
    total = 0.0
    number = 0
    count=0
    for line in numbersfile:
        try:
            number= float(line)
            count+= 1
            total= total+number
            print('i read in',count,'numbers' f' Current number is:     {number:.2f}     Total is: ',total)
        except ValueError:
            print('Non-numeric data found in the file. skipping..')
    numbersfile.close()

        
    average = total/count
    print('Average: ',average)

if __name__ == "__main__":
    main()
