
#Dictionary Programming Questions

#Basic

#1. Create a dictionary and print all keys and values.

d = {"name": "Mansi", "age": 21, "city": "Delhi"}

print("Keys:", d.keys())
print("Values:", d.values())

#2. Count frequency of each word in a sentence.

st = "apple mango apple banana mango"
words = st.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

print(d)

#3. Merge two dictionaries.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)

#4. Find the length of a dictionary.

d = {"a": 1, "b": 2, "c": 3}
print(len(d))

#5. Check if a key exists in a dictionary.

d = {"name": "Mansi", "age": 21}
if "age" in d:
    print("Key exists")
else:
    print("Not exists")

#OR
    
d = {"name": "Mansi", "age": 21}
print(d.get("age","Key not exists"))


#Intermediate

#6. Sort a dictionary by values.

d = {"a": 10, "b": 5, "c": 20}
values = list(d.values())
values.sort()

for v in values:
    for k in d:
        if d[k] == v:
            print(k, ":", v)

#7. Find the key with the maximum value.

d = {"a": 10, "b": 20, "c": 5}
max_value = 0
max_key = ""

for k in d:
    if d[k] > max_value:   #d[k] = "key k ki value"
        max_value = d[k]
        max_key = k

print("Max key:", max_key)

#8. Remove a key from a dictionary.

d={"a":1,"b":2,"c":3}
del d["b"]
print(d)

#OR

d = {"a": 1, "b": 2, "c": 3}
d.pop("b")  # removes key, gives error if key not presen
print(d)

#9. Convert two lists into a dictionary.

keys=["a","b","c"]
values=[1,2,3]
d=dict(zip(keys,values))
print(d)

#10. Count character frequency using a dictionary.

s = "hello"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


#Tricky

#11. Invert a dictionary (swap keys and values).

d = {"a": 1, "b": 2}  # key-value
inv = {}
for k in d:
    v = d[k]
    inv[v] = k  #value-key
print(inv)

#12. Group elements by frequency using a dictionary.

nums=[1,2,2,3,3,3]
freq={}
for n in nums:
    freq[n]=freq.get(n,0)+1
group={}
for k,v in freq.items():
    if v not in group:
       group[v]=[]
    group[v].append(k)
print(group)

#13. Find duplicate values in a dictionary.

d={"a":1,"b":2,"c":1}
seen=set()
duplicates=set()
for v in d.values():
    if v in seen:
        duplicates.add(v)
    else:
        seen.add(v)
print(duplicates)

#14. Create a nested dictionary for student records.

students={"John":{"age":20,"marks":85},
          "Anna":{"age":21,"marks":90}}
print(students["John"]["marks"])

#15. Flatten a nested dictionary.

d = {
    "a": 1,
    "b": {"x": 10, "y": 20}
}

flat = {}
for k in d:
    if type(d[k]) == dict:
        for k2 in d[k]:
            flat[k + "_" + k2] = d[k][k2]
    else:
        flat[k] = d[k]
print(flat)

#Mixed (String + Set + Dictionary)

#1. Count unique words in a sentence.

st = "apple mango apple banana mango"
words = st.split()     #convert into words
unique = set(words)    #remove duplicate 
print(len(unique))

#2. Find common characters between two strings.

s1 = "hello"
s2 = "world"
common = set(s1) & set(s2)
print(common)

#3. Find the most frequent character in a string.

st = "aaabbbbbcc"

max_char = st[0]
max_count = st.count(st[0])

for ch in st:
    if st.count(ch) > max_count:
        max_count = st.count(ch)
        max_char = ch

print(max_char)

#4. Remove duplicate words from a sentence.

st = "apple mango apple banana mango"
words = st.split()
new = []
for w in words:
    if w not in new:
        new.append(w)
        
print(" ".join(new))

#5. Find words with the same letters (anagram groups).

words = ["listen", "silent","rat", "tar", "bat"]
groups = {}

for w in words:
    key = "".join(sorted(w))   #sort letters of word alphabetically to create a common key 

    if key not in groups:
        groups[key] = []

    groups[key].append(w)

print(groups.values())

