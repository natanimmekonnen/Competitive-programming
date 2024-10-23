# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
    
        indexes = list(range(len(nums)))
        
        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)
            temp = []
            i, j = start, mid
            right_count = 0
            while i < mid and j < end:
                if nums[indexes[j]] < nums[indexes[i]]:
                    temp.append(indexes[j])
                    right_count += 1
                    j += 1
                else:
                    result[indexes[i]] += right_count
                    temp.append(indexes[i])
                    i += 1
        
            while i < mid:
                result[indexes[i]] += right_count
                temp.append(indexes[i])
                i += 1
            while j < end:
                temp.append(indexes[j])
                j += 1
        
            for i in range(start, end):
                indexes[i] = temp[i - start]
    
        merge_sort(0, len(nums))
        return result
            