import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,6,7,8,9])
sum = arr1+arr2
print(sum)
l1 = [int(x) for x in arr1]
l2 = [int(x) for x in arr2]
print(l1, l2)
l1.extend(l2)
print(l1)

new_arr = np.concatenate([arr1,arr2])
print(new_arr)