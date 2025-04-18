set1 = set("abcdefg")
set2 = set("adegjke")
set3 = set("aaaaaaaaa")

print(set1)
print(set2)
print(set3) 


set1.intersection(set2)
set1.union(set2)
set1.difference(set2)       
set1.symmetric_difference(set2)
print("Intersection:", set1.intersection(set2))
print("Union:", set1.union(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))
set4 =set1.symmetric_difference(set2)
set4.isdisjoint(set1)
print("Is disjoint:", set4.isdisjoint(set1))
set4.isdisjoint(set3)
print("Is disjoint:", set4.isdisjoint(set3))



# Adding, removing, and popping elements
set1.add('h')
print("After adding 'h':", set1)

set1.remove('a')
print("After removing 'a':", set1)

set1.discard('z')  # No error if 'z' is not present
print("After discarding 'z':", set1)

popped = set1.pop()
print("Popped element:", popped)
print("After popping an element:", set1)

set1.clear()
print("After clearing the set:", set1)

# A. the set are mutable
# B. the set are unordered
# C. the are not indexed
# D. the set are iterable
# E. the set length can be found using the len() function
# F. yes

