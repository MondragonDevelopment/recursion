import numpy as np

def sum(array):
    if len(array)==0:
        return 0
    else:
        head = array[0]
        tail = array[1:]
        return sum(tail) + head


nums = np.array([1,2,3,4,5,6])
print(sum(nums))
