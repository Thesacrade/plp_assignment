'''
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.
'''
from operator import indexOf

my_list = []
elements= [10, 20, 30, 40]
for i in elements:
    my_list.append(i)
print (my_list)
my_list.insert(1, 20)
second_list = [50, 60, 70]
my_list.extend(second_list)
my_list.pop()
my_list.sort()
print(my_list.index(30))
