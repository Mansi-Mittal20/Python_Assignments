#Python Programming Questions – TUPLE 
#Basic Level

#1. Write a Python program to create a tuple and print its elements.

t=(67,78,45,60)
print(t)

#2. Write a program to find the length of a tuple.

t=(67,78,45,60)
print (len(t))

#3. Write a program to find the maximum and minimum element in a tuple.

t=(67,78,45,60)
print (max(t))
print (min(t))

#4. Write a program to convert a tuple into a list.

t = (10, 20, 30, 40)
li = list(t)
print(li)

#5. Write a program to check if an element exists in a tuple.

t = (50, 20, 80, 40)
num = int(input("Enter number: "))
if num in t:
    print("Element exists")
else:
    print("Not found")

#6. Write a program to count occurrences of an element in a tuple.

t=(45,78,34,78,80,23,45)
num = int(input("Enter number: "))
count = 0

for i in t:
    if i == num:
        count = count + 1
print("Number", num, "appears", count, "times")

#Intermediate Level

#7. Write a program to slice a tuple and display the result.

t=(45,78,34,78,80,23,45)
print(t)
print(t[2:5])

#8. Write a program to find repeated elements in a tuple.

t = (1, 2, 3, 2, 4, 5, 1)
repeated = []

for i in t:
    if t.count(i) > 1 and i not in repeated:
        repeated.append(i)

print("Repeated elements:", repeated)

#9. Write a program to merge two tuples.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("Merged tuple:", merged)

#10. Write a program to unpack elements of a tuple into variables.

t = (10, 20, 30)
a, b, c = t
print("a =", a)
print("b =", b)
print("c =", c)

#11. Write a Python program to sort a tuple.

t = (5, 2, 8, 1, 3)
sorted_tuple = tuple(sorted(t))
print("Sorted tuple:", sorted_tuple)

#12. Write a program to convert a list of tuples into a dictionary.

list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
d = dict(list_of_tuples)
print("Dictionary:", d)


#Advanced Level

#13. Write a program to find the index of an element in a tuple.

t = (10, 20, 30, 40)
num = int(input("Enter number: "))
if num in t:
    print("Index =", t.index(num))
else:
    print("Element not found")

#14. Write a program to remove an element from a tuple (without directly modifying it).

t = (10, 20, 30, 40)
num = int(input("Enter number to remove: "))
new_t = ()
for i in t:
    if i != num:
        new_t = new_t + (i,)   # (i,)ye hume , tuple ke liye use kiya h
print("New tuple:", new_t)

#15. Write a program to find common elements between two tuples.

t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)
for i in t1:
    if i in t2:
        print("Common:",i)

#16. Write a Python program to check if a tuple is a palindrome.

t = (1, 2, 3, 2, 1)

if t == t[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#17. Write a program to find the element with maximum frequency in a tuple.

t = (1,5,5,78,9,4,653,2,4,6,78,6,4,4,5,3,45,6,7,56,4,4)
maxx = t.count(t[0])
e = t[0]
for m in t:
    if maxx<t.count(m):
        maxx = t.count(m)
        e = m
print( e, maxx )

#18. Write a program to create a nested tuple and access its elements.

t=((1,2,3),8,(4,5,6),7)

print(t[0])     
print(t[2])      
print(t[2][1])
print(t[3])
