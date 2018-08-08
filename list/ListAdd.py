l = [10, 5, 8 , 7]
l.append(40);
l.append(30)

print('After Append : ', l)

l.insert(1, "A")
l.insert(5, "B")
print('\nAfter Insert : ', l)

l2 = [40,60,80,70]
l.extend(l2)
print('\nAfter Extending list : ', l)

#Difference between insert() append() and extend()