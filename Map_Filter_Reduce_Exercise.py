#Map_Filter_Reduce_Lambda_Exercise

#Beginner Level

#1. Lambda Basics

#o Write a lambda function to add two numbers.

add=lambda a,b:a+b
print(add(2,3))

#o Write a lambda function to check if a number is even or odd.

even_odd=lambda x: "Even" if x%2==0 else "Odd"
print(even_odd(4))

#2. Using map()

#o Given a list of integers, use map() to create a new list with each number squared.

num=[1,2,3,4]
result=list(map(lambda x: x**2,num))
print(result)

#o Convert a list of strings to uppercase using map().

words=["hello","world"]
result=list(map(lambda x: x.upper(),words))
print(result)

#3. Using filter()

#o Given a list of numbers, filter out only even numbers.

nums=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,nums))
print(result)

#o Filter words that have length greater than 5 from a list of strings.

words=["apple","banana","kiwi","orange"]
result=list(filter(lambda x: len(x)>5,words))
print(result)

#4. Using reduce()

#o Find the sum of all elements in a list using reduce().

from functools import reduce
lst = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y,lst)
print(result)

#o Find the product of all numbers in a list.

from functools import reduce
lst = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, lst)
print(result)

#Intermediate Level

#5. Combination of lambda + map

#o Given a list of numbers, return a list where each number is multiplied by 10.

nums=[1,2,3,4]
result=list(map(lambda x:x*10,nums))
print(result)

#6. Combination of lambda + filter

#o From a list of numbers, filter out all numbers divisible by 3.

nums=[1,3,4,6,7,9,10]
result=list(filter(lambda x:x%3==0,nums))
print(result)

#7. Using reduce() for maximum

#o Find the maximum number in a list using reduce().

from functools import reduce
nums=[5,2,9,1]
result=reduce(lambda x,y:x if x>y else y,nums)
print(result)

#8. String Manipulation

#o Given a list of names, use map() to return names with their first letter capitalized.

names=["sakshi","rahul","priya"]
result=list(map(lambda x: x.capitalize(),names))
print(result)

#9. Filter Palindromes

#o Given a list of strings, filter out only palindrome words using filter().

words=["madam","hello","level"]
result=list(filter(lambda x:x==x[::-1],words))
print(result)
