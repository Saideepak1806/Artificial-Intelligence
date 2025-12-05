nested_list = [1, 2, [3, 4, 5], 6]
print("Nested List:", nested_list)

print("Length of list:", len(nested_list))

a = [10, 20]
b = [30, 40]
c = a + b
print("Concatenation:", c)

print("Is 20 in a?:", 20 in a)
print("Is 50 in a?:", 50 in a)

print("Iterating through list c:")
for item in c:
    print(item)

print("First element:", c[0])
print("Last element:", c[-1])

print("Slice c[1:3]:", c[1:3])
print("Slice c[:2]:", c[:2])
print("Slice c[2:]:", c[2:])
