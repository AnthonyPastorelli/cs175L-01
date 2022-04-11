import matplotlib.pyplot as plt


def main():
    infile= open('expenses.txt','r')
    labels=[]
    values=[]
    for line in infile.readlines():
        line=line.replace('Payment', '')
        labels.append(str(line.split()[0]))
        values.append(int(line.split()[1]))
    plt.pie(values, labels=labels, colors=('c','y','b','r','m','g'))
    plt.show()


main()
