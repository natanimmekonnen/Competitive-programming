# Problem: c - Reposts - https://codeforces.com/gym/533316/problem/c

from sys import stdin, stdout

num_reposts = int(stdin.readline().rstrip())

repost_tree = {}

for _ in range(num_reposts):
    line = stdin.readline().rstrip()
    reposter, original_poster = line.split(' reposted ')
    reposter, original_poster = reposter.lower(), original_poster.lower()
    if original_poster not in repost_tree:
        repost_tree[original_poster] = []
    repost_tree[original_poster].append(reposter)

repost_depth = {"polycarp": 1}
most_popular = "polycarp"
processing_queue = ["polycarp"]

while processing_queue:
    current, processing_queue = processing_queue[0], processing_queue[1:]
    if current not in repost_tree:
        continue
    for reposter in repost_tree[current]:
        repost_depth[reposter] = 1 + repost_depth[current]
        if repost_depth[reposter] > repost_depth[most_popular]:
            most_popular = reposter
        processing_queue.append(reposter)

print(repost_depth[most_popular])