list1 = [1, 2, 3, 4]
list2 = list1

print(list1, list2)
print(list1, list2)
list1[0] = list2[0]
print(list1, list2)
list2[0] = 200
print(list1, list2)