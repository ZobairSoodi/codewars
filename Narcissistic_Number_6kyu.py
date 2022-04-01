import math


def nar(n):
    temp_str = str(n)
    temp_len = len(temp_str)
    sum = 0
    for i in temp_str:
        sum += math.pow(int(i), temp_len)
    if (sum == n):
        return True
    return False
