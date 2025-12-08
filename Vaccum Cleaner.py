rooms = {"A":"dirty","B":"dirty"}
loc = "A"

while "dirty" in rooms.values():
    if rooms[loc] == "dirty":
        rooms[loc] = "clean"
    else:
        loc = "B" if loc=="A" else "A"

print(rooms)
