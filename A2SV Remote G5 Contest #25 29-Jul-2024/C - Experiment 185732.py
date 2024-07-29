# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C


def minimum_rooms(experiments):
    events = []

    for s, t, b in experiments:
        events.append((s, b))
        events.append((t + 1, -b))

    events.sort(key=lambda x: (x[0], x[1]))

    max_rooms_needed = 0
    current_rooms_in_use = 0

    for time, room_change in events:
        current_rooms_in_use += room_change
        if current_rooms_in_use > max_rooms_needed:
            max_rooms_needed = current_rooms_in_use

    return max_rooms_needed

n = int(input())
experiments = []

for _ in range(n):
    s, t, b = map(int, input().split())
    experiments.append((s, t, b))

print(minimum_rooms(experiments))