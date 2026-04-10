#Python Programming Questions – LIST

#Intermediate Level

#1. Write a program to merge two lists and remove duplicates.

l1 = [11, 26, 32, 48]
l2 = [32, 48, 57, 60]

merged = l1 + l2
result = []

for i in merged:
    if i not in result:
        result.append(i)

print(result)

#2. Write a program to find common elements between two lists.

l1 = [11, 24, 39, 47]
l2 = [39, 47, 52, 65]

for i in l1:
    if i in l2:
        print(i)

#3. Write a program to split a list into even and odd numbers.

li = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)
        
#4. Write a program to rotate a list by n positions.

li = [1,2,3,4,5,6,7,8,9,10]
print( li )
n = int(input("No of Right Rotation : "))
for i in range(n):
    val = li.pop(len(li)-1)
    li.insert(0,val)
print(li)

#5. Write a Python program to find the second largest number in a list.

li = [1, 2, 4, 48, 19]

max1 = max(li)
li.remove(max1)

max2 = max(li)

print("Second largest:", max2)

#6. Write a program to flatten a nested list.

li = [[12,34,67],[5,6,89],[45,78,67]]
f_li = []
print("Nested List :",li)
for x in li:
    for i in x:
        f_li.append(i)
print("Flaten List :",f_li)

#OR

li = [[12,34],[5,6,89],72,[45,78,67]]
f_li = []
print("Nested List :",li)
for x in li:
    if type(x)==list:
        for i in x:
            f_li.append(i)
    else:
        f_li.append(x)
print("Flaten List :",f_li)


#7. Write a program to count frequency of each element in a list.

li = [10,25,25,33,33,33,40]
done = []
for i in li:
    if i not in done:
        print(i, "->", li.count(i))
        done.append(i)

#8. Write a program to replace all negative numbers with zero in a list.

li = [10, -5, 20, -3, 30]

for i in range(len(li)):
    if li[i] < 0:
        li[i] = 0

print(li)

#Advanced Level

#9. Write a program to remove all occurrences of a given element from a list.

li = [1,2,3,2,4,2,5]

num = int(input("Enter number to remove: "))

new_li = []

for i in li:
    if i != num:
        new_li.append(i)

print(new_li)

#10. Write a program to check if a list is a palindrome.

li = [1,4,3,4,1]

if li == li[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#11. Write a Python program to find missing numbers in a given list of consecutive integers.

li = [1, 2, 4, 6, 7]

for i in range(li[0], li[-1] + 1):      #range(1, 8) → 1,2,3,4,5,6,7
    if i not in li:
        print(i)
    
#12. Write a program to perform element-wise addition of two lists.

l1 = [1,2,3]
l2 = [4,5,6]

result = []

for i in range(len(l1)):
    result.append(l1[i] + l2[i])

print(result)
    
#13. Write a Python program to find the longest increasing subsequence in a list.
"""HINT:-
li = [21,78,89,765,23,23,35,39,45,667,8,9,635,58]"""

li = [21,78,89,765,23,23,35,39,45,667,8,9,635,58]
longest_sub_seq = []
temp = []
for i in range(0,len(li)-1):
    if li[i]<li[i+1]:
        temp.append(li[i])
    else:
        temp.append(li[i])
        if len(temp)>len(longest_sub_seq):
            longest_sub_seq = temp
        temp = []
print(longest_sub_seq)

#14. Write a program to group elements based on frequency.

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
group_list = []
selected = []
for x in li:
    if x not in selected:
        selected.append(x)
        for j in li:
            if x==j:
                group_list.append(j)
print(group_list)

#OR

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
s = set(li)
print(s)
group_list = []
for x in s:
    group_list.extend([x]*li.count(x))
print(group_list)

#OR

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
group_list = []
selected = []
for x in li:
    if x not in selected:
        selected.append(x)
        group_list.append( (x,li.count(x)) )    

print(group_list)

#OR

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
group_list = []
for x in set(li):
    group_list.append( (x,li.count(x)) )    

print(group_list)
