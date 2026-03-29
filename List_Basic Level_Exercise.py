#Python Programming Questions – LIST 
#Basic Level

#1. Write a Python program to create a list of integers and print its elements.

li=[34,45,67,82,78]
print(li)

#2. Write a program to find the sum and average of all elements in a list.

li=[34,45,67,82,20,27,78]
print(li)
print(sum(li))
print(sum(li)/len (li))

#3. Write a program to find the largest and smallest element in a list.

li=[34,45,67,82,20,27,78]
print(li)
print(max(li))
print(min(li))

#5. Write a program to reverse a list without using built-in functions.

li = [45, 67, 82, 20, 27, 78]
rev = []
for i in range(len(li)-1, -1, -1):
    rev.append(li[i])
    
print(rev)

#6. Write a program to check if an element exists in a list.

li=[35,20,38,56]
num=20

if num in li:
    print("Element exists")
else:
    print("Not found")

#7. Write a Python program to remove duplicate elements from a list.

li=[10,20,10,30,20,40]

new_list=[]

for i in li:
    if i not in new_list:
        new_list.append(i)

print(new_list)

#8. Write a program to sort a list in ascending and descending order.

li=[56,38,60,34,45,67,82,20,27,78]
li.sort()
print("Ascending:",li)

li.sort(reverse=True)
print("Descending:",li)
