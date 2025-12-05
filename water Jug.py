from collections import deque

A, B, T = 4, 3, 2
q = deque([(0,0)])
vis = set()

while q:
    x, y = q.popleft()
    if (x, y) in vis: continue
    vis.add((x, y))
    print(x, y)
    if x == T or y == T: break

    nxt = [
        (A, y), (x, B), (0, y), (x, 0),
        (max(0, x-(B-y)), min(B, y+x)),  # A → B
        (min(A, x+y), max(0, y-(A-x)))   # B → A
    ]
    q.extend(nxt)
