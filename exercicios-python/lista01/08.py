A = {1, 2, 3}
C = {1, 2, 3, 4, 5}

print(A.issubset(C) and A != C)  # A ⊂ C

D = {5, 3, 4, 2, 1}
print(D.issubset(C) and D != C)  # D ⊂ C
