# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {restaurant: index for index, restaurant in enumerate(list1)}
        min_index_sum = float('inf')
        result = []

        for index, restaurant in enumerate(list2):
            if restaurant in index_map:
                index_sum = index + index_map[restaurant]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_index_sum:
                    result.append(restaurant)

        return result

        