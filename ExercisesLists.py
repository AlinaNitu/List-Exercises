#1. Write a Python program to sum all the items in a list.

def sums(a):
    return sum(a)

#2. Write a Python program to multiplies all the items in a list.

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

#3. Write a Python program to get the largest number from a list.

def largest_number(a):
    b=sorted(a)
    return b[-1]

#4. Write a Python program to get the smallest number from a list.

def smallest_number(a):
    b=sorted(a)
    return b[0]

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

def lenght(a):
    n=0
    for char in a:
        if len(char)>=2:
            if char[0]==char[-1]:
                n+=1
    return n

#21. Write a Python program to convert a list of characters into a string.

def lst(a):
	b= ''.join(a)
	return b

#22. Write a Python program to find the index of an item in a specified list.

def word(a):
	indx=input('Specify the word or letter you want to find the index: ')
	result = a.index(indx)

	print(result)


#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7. Write a Python program to remove duplicates from a list.

def remove_duplicates(a):
    b=set(a) #using sets
    return b
def remove_duplicates2(a):
    b= []
    for elem in a:
        if elem not in b:
            b.append(elem)
    return b

#8. Write a Python program to check a list is empty or not.

def check_lst(a):
        if len(a)==0:
            print('This list is empty')
        else:
            print('The list has {} elements'.format(len(a)))

#9. Write a Python program to clone or copy a list.

def clone_list(a):
    a=input()
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)

#10. Write a Python program to find the list of words that are longer than n from a given list of words.

def longer(n, lst):
    b=[]
    for elem in lst:
        if len(elem)<=n:
            b.append(elem)
    return b

#11. Write a Python function that takes two lists and returns True if they have at least one common member.


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def remove(list1):
        list1.pop(5)
        list1.pop(4)
        list1.pop(0)
        return list1

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def no_evennumbers(a):
    return [num for num in a if num%2 != 0]

#15. Write a Python program to shuffle and print a specified list.

import random

def lst(a):
    random.shuffle(a)
    print('Reshuffled list: ', a)

#16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def square():
    b=[]
    for num in range(1,31):
        b.append(num**2)
    print(b[:5])
    print(b[-5:])

#17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

def square1():
    b=[]
    for num in range(1,31):
        b.append(num**2)
    print(b[5:])

#18. Write a Python program to generate all permutations of a list in Python.

import itertools

print(list(itertools.permutations([2,3,4])))

#19. Write a Python program to get the difference between the two lists.

def diff_lists(list1,list2):
    print(list(set(list1)-set(list2)))

#20. Write a Python program access the index of a list.

def index(list1):
    for x, y in enumerate(list1):
        print (x,y)

#21. Write a Python program to convert a list of characters into a string.

def listtostring(a):
    for elem in a:
        return ''.join(a)


#22. Write a Python program to find the index of an item in a specified list.

def list1(a):
    inp=input('What item would you like to find in the list?')

    for item in a:
        return a.index(inp)

