import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,6,7,8,9])
arr3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
sum = arr1+arr2
print(sum)
l1 = [int(x) for x in arr1]
l2 = [int(x) for x in arr2]
print(l1, l2)
l1.extend(l2)
print(l1)

new_arr = np.concatenate([arr1,arr2])
print(new_arr)

print(np.sum(arr1))
print(np.mean(arr1),np.mean(arr2))
print(np.max(arr1))
print(np.min(arr1))
print(np.std(arr1),np.std(arr2))
print(np.var(arr1),np.var(arr2))

#indexing and slicing
#indexing
print(arr1[0])  #1d array
print(arr3[2,1]) #2d array
#slicing
print(arr1[0:4:1]) #expected output:from index:0 to index3 1,2,3,4
print(arr1.reshape(5,1))
#converting multi dimenstinal arrays into 1d arrays
#ravel() returns veiw,flatten() returns copy
print(arr3.flatten())
#inserting values
print(arr1)
arr4 = np.insert(arr1, 2, 100)
print(arr4)  #1d arrays
print(arr3)
arr5 = np.insert(arr3, 3, [100], axis=1)
print(arr5)
#append
arr6 = np.append(arr1, [23,45,67])
print(arr6)
#concatenate
arr7 = np.concatenate((arr1, arr2))
print(arr7)
#delete
arr8 = np.delete(arr1, 0)
print(arr8)
#stacking
#vstack = vertically stacking
#hstack = horizontally stacking
print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))
dt = np.genfromtxt('dt.txt', delimiter=',')

print("NumPy Array:")
print(dt)