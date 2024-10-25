# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n, pairs = len(nums1), 0
        nums = [x1 - x2 for x1, x2 in zip(nums1, nums2)]
        i_nums = SortedList()      
        for j_num in nums:
            pairs += i_nums.bisect_right(j_num + diff)
            i_nums.add(j_num)
			
        return pairs