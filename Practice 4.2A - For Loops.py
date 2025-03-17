#Python's for statements iterates over the items of any sequence (strings, lists) in the order that they appear in the sequence.
words = ["cat", "dog", "lizard", "fish", "elephant", "octopus"]
for elements in words:
    print(elements, f"is {len(elements)} letters long!")

#Code that modifies a collection while iterating over that same collection can be tricky to get right.
#It's more straightforward to create a copy of the collection or create a new collection.
users = {"Hans":"active", "Eleanor":"active", "Teddy":"inactive", "Mark":"inactive"}

#Creating a copy:
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)

#Creating a new collection:
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)
