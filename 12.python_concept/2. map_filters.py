import math

"""
you can use on iterable objects
map - iterbake to new value
filter - specific values in iterable objects

"""

lst = [1, 2, 3, 4, 5, 6, 7]
# generte list of square
# list comprehension
# for loops
# better way involving map functions
x_lst = map(lambda x: x**2, lst)
"""
map function is going to loop through
every single objects in my iterable objects
and called lambda functions on it
pass for x every single items individually
start by passing 1 and this would be return
1^2
"""
print(x_lst)
# we get map objects <map object at 0x102176ce0>
# map func return an iterable obejcts if want
# list you have to convert like this
new_lst = list(map(lambda x: x**2, lst))
print(new_lst)

# 2nd way to loop through map objects
# iterable obejcts
for x in x_lst:
    print(x)

x_lst = list(map(lambda x: math.sqrt(x), lst))
print(x_lst)

lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
# lambda return sum(x)
new_lst = list(map(lambda x: sum(x), lst))
print(new_lst)

# filter give you value which satisfy specific constraints
lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
# greater than sum 6 the internal list
new_lst = filter(lambda x: sum(x) > 6, lst)
for el in new_lst:
    print(el)

new_lst = list(filter(lambda x: sum(x) > 6, lst))
print(new_lst)


new_lst = list(filter(lambda x: True, lst))
# geeting all the items
print(new_lst)

# return False
new_lst = list(filter(lambda x: False, lst))
# geeting None the items
print(new_lst)

new_lst = list(filter(lambda x: len(x) > 2, lst))
# geeting len greate than 2 items
print(new_lst)

# how to use map and filter together
# func to filter it  map(lambda x: sum(x), lst
new_lst = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), lst))
print(list(new_lst))
