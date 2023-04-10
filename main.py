import numpy as np
from test import test
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
    ins = 0.01
    x = np.array(test())
    m_x = np.mean(x)


    n = x.size
    sum = 0
    for num in np.nditer(x):
        sum += pow((num - m_x), 2)
    tp = [1.84, 1.32, 1.20, 1.14, 1.11, 1.09, 1.08, 1.07, 1.06, 1.05, 1.04, 1.03, 1.00]
    sigma = sqrt(sum / (n - 1))
    ua = tp[nFliter(n)] * sqrt(sum /n / (n - 1))
    ub = ins / sqrt(3)
    u1sigma = sqrt(pow(ua, 2) + pow(ub, 2))
    u2sigma = 2 * u1sigma
    sigmarange = [m_x - 3 * sigma, m_x + 3 * sigma]
    print(m_x, sigma, sigmarange, ua, ub, u1sigma, u2sigma)
  
if __name__ == "__main__":
    main()