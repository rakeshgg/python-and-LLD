"""
List, tuple, dict....


"""

x = [1, 2, 3]
# call iter functions on x and return
# Iterable
"""
for val in x: is equivalent to say
give me the iterator equivalent to x
and use that iterator to get next value
in my sequence
"""
for val in x:
    print(val)


x_iter = iter(x)
# give itarbale obejcts
print(x_iter)
# <list_iterator object at 0x1027b6d10>
# list_iterator
# how to get next value
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
# print(next(x_iter))  # StopIteration Exception get

x = [1, 2, 3]
"""
when using for loops you are getting syatx like this
python source code
"""
x_iter = iter(x)
while True:
    try:
        print(next(x_iter))
    except StopIteration:
        break

"""
what make iterable obejcts as iterator
that has special methods __iter__
x_iter = x.__iter__()
same as
iter(x)

"""

x_iter = x.__iter__()
while True:
    try:
        # print(next(x_iter))
        print(x_iter.__next__())
    except StopIteration:
        break


# how to make our own iterator
class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __iter__(self):
        return NumberIterator(self.num1, self.num2, self.num3)


class NumberIterator:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        elif self.current == 2:
            return self.two
        elif self.current == 3:
            return self.three
        else:
            raise StopIteration


# how to use
nums = Numbers(1, 2, 3)
itr = iter(nums)
# print(itr)
# <__main__.NumberIterator object at 0x10493b250>
print(next(itr))
print(next(itr))
# print(next(itr))

nums = Numbers(1, 2, 3)
for num in nums:
    print(num)

"""
numbers class iterable itself rather than two class
not a best practise, making same
"""


class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.current = 0

    def __iter__(self):
        self.current = 0
        # return same obejcts back
        # on same obejcts next is defiend so we can iterate
        return self

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.num1
        elif self.current == 2:
            return self.num2
        elif self.current == 3:
            return self.num3
        else:
            raise StopIteration


nums = Numbers(1, 2, 3)
for num in nums:
    print(num)
"""
Problem is we don't have seperate iterators
with different internal states. previously
returng differnt iterable obejcts here returing
same iterbale obejcts we cannot have multiple
iterators representing this state

"""
num_iter_1 = iter(nums)
print(next(num_iter_1))
# op 1
num_iter_2 = iter(nums)
print(next(num_iter_2))
# num_iter_1, num_iter_2 same iterator objects
# having same internal states so chnges reflect one
# both previous one both are differnt iterators
# op 1
# num_iter_1 = iter(nums)
