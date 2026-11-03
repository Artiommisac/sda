class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
                
            if right < n and arr[right] > arr[largest]:
                largest = right
                
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        n = len(nums)
        
        # Step 1: Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)
            
        # Step 2: Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Move root to the end
            heapify(nums, i, 0)                 # Heapify the reduced heap
            
        return nums