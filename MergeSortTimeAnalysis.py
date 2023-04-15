import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer
z=[k for k in range(10,110,10)]
zt=[]
for n in z:
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

    data = []

    for a in range(0,n):
        data.append(random.randint(1, 100))

    mergeSort(data)
    end = timer()
    zt.append(end-start)

plt.plot(z,zt)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Time analysis of Merge Sort")
plt.show()
