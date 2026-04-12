#String Programming Questions

#Basic

#1. Write a program to count the number of vowels in a string.

st = "amankumar"
count = 0

for i in st:
    if i in "aeiouAEIOU":
        count += 1

print("Vowels:", count)

#2. Reverse a string without using built-in functions.

st = "MANSI"
rev = ""

for i in st:
    rev = i + rev

print(rev)

#3. Check whether a string is a palindrome.

st = "NAMAN"
print(st)
if st==st[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#4. Count uppercase and lowercase letters in a string.

st = "ManSiMIttAL"

upper = 0
lower = 0

for i in st:
    if i >= 'A' and i <= 'Z':
        upper += 1
    elif i >= 'a' and i <= 'z':
        lower += 1
        
print("Uppercase:", upper)
print("Lowercase:", lower)
    
#5. Replace all spaces in a string with _.

st = "Hello Mansi "
new = ""

for i in st:
    if i == " ":
        new = new + "_"
    else:
        new = new + i

print(new)
    

#Intermediate

#6. Find the frequency of each character in a string.

st = "aabbc"
done = ""

for i in st:
    if i not in done:
        print(i, "->", st.count(i))
        done = done + i
    
#7. Remove duplicate characters from a string.

st="mansimittal"
new=""
for i in st:
    if i not in new:
        new=new+i
print(new)
    
#8. Find the first non-repeating character in a string.

st = "amankumar"
for i in st:
    if st.count(i)==1:
        print("First Non-Repeating Charcter :",i)
        break
else:
    print("No Non-Repeating Character")

#9. Check if two strings are anagrams.

#hint: LISTEN , SILENT

st1 = "SILENT"
st2 = "LISTEN"
if len(st1)==len(st2):
    for ch in st1:
        if st1.count(ch)!=st2.count(ch):
            print("Strings Are Not Anagram")
            break
    else:
        print("Strings Are Anagram")
else:
    print("Strings Are Not Anagram!")
    
#10. Convert "hello world" → "Hello World" (title case without using .title()).

st = "hello mansi"
new = ""

for i in range(len(st)):
    if i == 0 or st[i-1] == " ":   #st[i-1] checks if previous character is space
        new = new + st[i].upper()
    else:
        new = new + st[i]

print(new)
    
    
#Tricky
    
#11. Find the longest word in a sentence.

st = "I love python"
words = st.split()  #split makes words
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)
    
#12. Compress a string like "aaabbc" → "a3b2c1".

st = "aaabbc"
i = 0
count = 1
temp = ""
while i<len(st)-1:
    if st[i]==st[i+1]:
        count+=1
    else:
        temp = temp+st[i]+str(count)
        count = 1
    i=i+1
temp = temp+st[i]+str(count)
print(temp)

    
#13. Count words, characters, and digits in a string.

st = "Aman123 Kumar"
words = 1
digits = 0
chars = 0
for i in st:
    if i != " ":
        chars += 1
    if i >= '0' and i <= '9':
        digits += 1
    if i == " ":
        words += 1

print("Words:", words)
print("Characters:", chars)
print("Digits:", digits)

#14. Rotate a string left by n positions.

st = "AMANKUMAR"
print(st)
n = int(input("No of position by left : "))
for i in range(n):
    st = st[1:]+st[0]
print(st)

#OR

st = "AMANKUMAR"
print(st)
n = int(input("No of position by left : "))
st = st[n:]+st[0:n]
print(st)

    
#15. Find all substrings of a given string.
"""
Hint:AMAN
A
AM
AMA
AMAN"""

st = "AMAN"
for i in range(len(st)):        
    for j in range(i, len(st)):
        print(st[i:j+1])
 
