import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer
z = [k for k in range(0, 100, 10)]
zt = []

for n in z:
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

    data = []
    for a in range(0, n):
        data.append(random.randint(1, 100))

    size = len(data)

    quickSort(data, 0, size - 1)

    end = timer()
    zt.append(end-start)


plt.plot(z, zt)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Time analysis of Quick Sort")
plt.show()
