import numpy as np
from math import sqrt
from math import pow

def nFliter(n):
    if (n <= 10):
        return n - 2
    elif (n == 15):
        return 9
    elif (n == 20):
        return 10
    elif (n == 30):
        return 11
    else:
        return 12
  
def main():
    # data
    n = 5
    sum = 0
    ins = 0.02
    x = np.array([99.58, 99.62, 99.60, 99.58, 99.62])
    m_x = np.mean(x)


    for num in np.nditer(x):
        sum += pow((num - m_x), 2)
    tp = [1.84, 1.32, 1.20, 1.14, 1.11, 1.09, 1.08, 1.07, 1.06, 1.05, 1.04, 1.03, 1.00]
    ua = tp[nFliter(n)] * sqrt(sum /n / (n - 1))
    ub = ins / sqrt(3)
    u1theta = sqrt(pow(ua, 2) + pow(ub, 2))
    u2theta = 2 * u1theta
    print(ua, ub, u1theta, u2theta)
  
if __name__ == "__main__":
    main()