import csv
import numpy as np
import matplotlib.pyplot as plt


def linear_regression(x, y):     
    x_mean = x.mean()
    y_mean = y.mean()
    
    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean)**2).sum()
    B1 = B1_num / B1_den
    
    B0 = y_mean - (B1*x_mean)
    
    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))
    
    return (B0, B1, reg_line)

def corr_coef(x, y):
    N = len(x)

    num = (N * (x * y).sum()) - (x.sum() * y.sum())
    den = np.sqrt(
        (N * (x**2).sum() - x.sum() ** 2) * (N * (y**2).sum() - y.sum() ** 2)
    )
    R = num / den
    return R


def plot_regression_line(x, y, b):
    plt.scatter(x, y, color="m", marker="o", s=30)

    y_pred = b[0] + b[1] * x

    plt.plot(x, y_pred, color="g")

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


def main():
    with open('./regression.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        x = []
        y = []
        for row in reader:
            try:
                x.append(int(row[0]))
                y.append(int(row[1]))
            except: 
                continue
    x = np.array(x)
    y = np.array(y)
    B0, B1, reg_line = linear_regression(x, y)
    print("Regression Line: ", reg_line)
    R = corr_coef(x, y)
    print("Correlation Coef.: ", R)
    print('"Goodness of Fit": ', R**2)
    plot_regression_line(x, y, (B0, B1))


if __name__ == "__main__":
    main()