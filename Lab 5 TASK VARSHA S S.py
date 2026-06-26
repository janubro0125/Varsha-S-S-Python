'''
print("1.Largest & Smallest in list:")
l = []
n = int(input("Enter length: "))
for i in range(n):
    elements = int(input("Enter elements: "))
    l.append(elements)
print(l)

highest = l[0]
smallest=l[0]
for i in l:
    if i>highest:
        highest=i
for j in l:
    if j < smallest:
        smallest = j
print("Highest value:",highest)
print("Smallest value:", smallest)
'''
'''
print("2.Second largest element:")
l = []
n = int(input("Enter length: "))
for i in range(n):
    elements = int(input("Enter elements: "))
    l.append(elements)
print(l)

highest = l[0]
second = l[0]

for i in l:
    if i > highest:
        highest = i

for j in l:
    if j > second and j != highest:
        second = j

print("Second highest value:", second)
'''
'''
print("3.Remove Duplicate element:")
l = []
n = int(input("Enter length: "))
for i in range(n):
    elements = int(input("Enter elements: "))
    l.append(elements)
print("Original List:",l)
new_list=[]
for i in l:
    if i not in new_list:
            new_list.append(i)
print("List after removing duplicates:",new_list)
'''
