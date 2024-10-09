# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums) - 1, nums)

    def merge(self, left_half: List[int], right_half: List[int]) -> List[int]:
        result = []
        i, j = 0, 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
        
        while i < len(left_half):
            result.append(left_half[i])
            i += 1
        
        while j < len(right_half):
            result.append(right_half[j])
            j += 1
        
        return result

    def mergeSort(self, left: int, right: int, arr: List[int]) -> List[int]:
        if left == right:
            return [arr[left]]
        
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)
        
        return self.merge(left_half, right_half)
