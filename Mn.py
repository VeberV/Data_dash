A = {'ID453', 'ID312', 'ID41', 'ID3', 'ID500', 'ID920', 'ID36', 'ID27'}
B = {'ID41', 'ID36', 'ID27', 'ID124', 'ID7', 'ID501', 'ID91' }
union_AB = A.union(B) # union_AB = A | B объединение множеств
print(union_AB)
inter_AB = A.intersection(B) # inter_AB = A & B пересечение множеств
print(inter_AB)
diff_AB = A.difference(B) # diff_AB = A - B разность множеств
print(diff_AB)
symmAB = A.symmetric_difference(B) # symmAB = A ^ B симметрическая разность 
print(symmAB)
