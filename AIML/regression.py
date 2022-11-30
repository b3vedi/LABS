import csv

def lin_reg():
    with open('./regression.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            print(', '.join(row))

if (__name__ == "__main__"):
    lin_reg()