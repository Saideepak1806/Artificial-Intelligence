A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)


print("Union (A ∪ B):", A | B)

print("Intersection (A ∩ B):", A & B)

print("Difference (A - B):", A - B)

print("Symmetric Difference:", A ^ B)

print("Is 3 in A?:", 3 in A)
print("Is 7 in A?:", 7 in A)

print("Is A subset of B?:", A.issubset(B))
print("Is A superset of B?:", A.issuperset(B))

A.add(10)
print("After adding 10 to A:", A)

A.remove(2)
print("After removing 2 from A:", A)
