#Set Programming Questions

#Basic

#1. Create a set and add elements dynamically.

s=set()
s.add(50)
s.add(30)
s.add(90)
s.add(40)
s.add(70)
print(s)


#2. Find the union and intersection of two sets.

s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("UNION",s1|s2)
print("INTERSECTION", s1&s2)

#3. Remove duplicate elements from a list using a set.

li = [1,2,2,3,3,4]
s = set(li)
print(s)

#4. Check if an element exists in a set.

s={4,5,6,7,8}
if 5 in s:
    print("Element Exists")
else:
    print("Element Not Exists")

#5. Find the difference between two sets.

s1 = {1,2,3,4}
s2 = {3,4,5}
print("s1 - s2:", s1 - s2)
print("s2 - s1:", s2 - s1)    

#Intermediate

#6. Find common elements in two lists using sets.

l1 = [1,2,3,4]
l2 = [3,4,5,6]
s1 = set(l1)
s2 = set(l2)

print(s1 & s2)  # print(s1.intersection(s2))

#7. Check whether one set is a subset of another.

s1 = {1,2}
s2 = {1,2,3,4}
if s1.issubset(s2):
    print("Subset")
else:
    print("Not Subset")

#8. Find symmetric difference of two sets.

s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("symmetric difference", s1 ^ s2)
    
#9. Count unique elements in a list using a set.

li = [1,2,2,3,3,4]
s = set(li)
print("Unique count:", len(s))

#10. Remove all common elements from two sets.

s1 = {1,2,3,4}
s2 = {3,4,5,6}

common = s1 & s2

s1 = s1 - common
s2 = s2 - common

print("s1:", s1)
print("s2:", s2)


#Tricky

#11. Find missing numbers from 1 to n using sets.

li = [1,2,4,6]
n = 6

full = set(range(1, n+1))
given = set(li)

missing = full - given

print(missing)

#12. Check if two lists have any common elements.

l1 = [1,2,3]
l2 = [4,5,6,3]

if set(l1) & set(l2):
    print("Common elements present")
else:
    print("No common elements")

#13. Convert a set of strings into uppercase.

s = {"raam", "mansi", "poonam"}
new = set()

for i in s:
    new.add(i.upper())

print(new)    
    
#14. Identify unique vowels in a given string using a set.

st = "amankumar"

vowels = set()

for i in st:
    if i in "aeiou":
        vowels.add(i)

print(vowels)

#15. Find elements that appear only once in a list.

li = [1,2,2,3,4,4,5]
for i in set(li):
    if li.count(i) == 1:
        print(i)
