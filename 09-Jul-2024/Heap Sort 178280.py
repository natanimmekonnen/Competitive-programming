# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1


class Solution:
    def heapify(self,arr, n, i):
        largest = i  
        left = 2 * i + 1 
        right = 2 * i + 2 
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
            self.heapify(arr, n, largest)
    def buildHeap(self,arr,n):
        startIdx = n // 2 - 1
        for i in range(startIdx, -1, -1):
            self.heapify(arr, n, i)
    def HeapSort(self, arr, n):
        n = len(arr)
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            self.heapify(arr, i, 0)
        



