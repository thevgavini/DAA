import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer
z=[k for k in range(10,500,10)]
zm=[]
zq=[]

for n in z:
    data = []
    for a in range(0,n):
        data.append(random.randint(1, 500))

    #MergeSort
    start=timer()
    def mergeSort(data):
        if len(data) > 1:
            r = len(data)//2
            L = data[:r]
            M = data[r:]
            mergeSort(L)
            mergeSort(M)
            i = j = k = 0
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = M[j]
                    j += 1
                k += 1
            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                data[k] = M[j]
                j += 1
                k += 1
    mergeSort(data)
    end = timer()
    zm.append(end-start)

    #QuickSort
    start = timer()
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1
        
    def quickSort(array, low, high):
        if low < high:

            pi = partition(array, low, high)

            quickSort(array, low, pi - 1)

            quickSort(array, pi + 1, high)
        
    
    size = len(data)
    quickSort(data, 0, size - 1)
    end = timer()
    zq.append(end-start)


plt.plot(z,zm, label="MergeSort")
plt.plot(z,zq, label="QuickSort")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Time analysis of Merge Sort")
plt.legend()
plt.show()
