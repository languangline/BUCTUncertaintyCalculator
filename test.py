import numpy as np
import math

def test():
    data = [0.00, 4.53, 8.94, 13.48, 17.93, 22.57, 27.02, 31.49, 35.89, 40.35]
    returnList = []
    for i in range(5):
        returnList.append(data[i + 5] - data[i])
    print(returnList)
    return returnList

if __name__ == "__main__":
    test()