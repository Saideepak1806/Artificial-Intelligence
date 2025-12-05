def safe(b, r, c):
    for i in range(c):
        if b[i] == r or abs(b[i]-r) == abs(i-c):
            return False
    return True

def solve(c, b):
    if c == 8: return True
    for r in range(8):
        if safe(b, r, c):
            b[c] = r
            if solve(c+1, b): return True
    return False

b = [-1]*8
solve(0, b)

print("8-Queen Solution:")
for r in range(8):
    row = ["Q" if b[c]==r else "." for c in range(8)]
    print(" ".join(row))
