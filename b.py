set1 = set("abcdefg")
set2 = set("adegjke")
set3 = set("aaaaaaaaa")

# i. {i, j}
seti = {'i', 'j'}
print("i. {i, j}:", seti)

# ii. {a, b, c}
setii= set1.intersection({'a', 'b', 'c'})
print("ii. {a, b, c}:", setii)

# iii. {i, j, n, o, p}
setiii = {'i', 'j', 'n', 'o', 'p'}
print("iii. {i, j, n, o, p}:", setiii)

# iv. {d}
setiv = set1.intersection({'d'})
print("iv. {d}:", setiv)

# v. {k, l, m, n, o, p}
setv = {'k', 'l', 'm', 'n', 'o', 'p'}
print("v. {k, l, m, n, o, p}:", setv)