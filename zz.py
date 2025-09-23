intervals = [[1,2], [1,2], [3,8], [4,5], [6,7]]

events = []
for s, e in intervals:
    events.append((s, 1))   # start
    events.append((e, -1))  # end

# Sort by time, and if same time: process end (-1) before start (+1)
events.sort(key=lambda x: (x[0], x[1]))

curr = 0
max_overlap = 0
for _, delta in events:
    curr += delta
    max_overlap = max(max_overlap, curr)

print(max_overlap)  # Output: 3