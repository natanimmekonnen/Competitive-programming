# Problem: B - Chef Jamie - https://codeforces.com/gym/537575/problem/B

def min_swaps(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    index_map = {value: idx for idx, value in enumerate(arr)}
    swaps = 0

    for i in range(n):
        while arr[i] != sorted_arr[i]:
            swap_idx = index_map[sorted_arr[i]]
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
            index_map[arr[swap_idx]] = swap_idx
            index_map[arr[i]] = i
            swaps += 1

    return swaps


n = int(input())
arr = list(map(int, input().split()))
print(min_swaps(arr))
