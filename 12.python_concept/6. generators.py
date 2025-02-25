"""
Generators is special type of iterators
previous one lec - Legeacy interator syntax(old way)
when you deal with iteratots accomplish with generator
"""


def gen():
    """
    yield key word is similar to return statements
    yiled pause the execution of functions and call agin
    and resume more left on.
    It maintains internal state of functions when hit
    yield keywords
    """
    yield 1
    yield 2
    yield 3


print(type(gen))
# <class 'function'>
print(gen())
# we got genrator obejcts
# <generator object gen at 0x102a40a90>
"""
when u call func having yield keywords
it actually give you the generator obejcts
which is very similar to iterator both gen
and iterator have next methods defined on it

"""
itr = gen()
print(next(itr))
# when call next 1st yield run and pause
# excution and mintain internal state of functions
print(next(itr))
# when call next the 2nd yield run
print(next(itr))
# print(next(itr))
# StopIteration
itr = gen()
for i in itr:
    print(i)


# generator generate sequnce of value
# def fib(n):
#    pass


"""
fib_numbers = [1, 1]
for i in range(2, 100):
    last = fib_numbers[i - 1]
    second_last = fib_numbers[i - 2]
    num = last + second_last
    fib_numbers.append(i)
print(fib_numbers)
# very effiecient storing all numbers in List
# as its infinte sequnce
# why storing all numbers only last two are required
# inefficient memory utilizations
"""


def fib(n):
    last = 1
    second_last = 1
    current = 3
    while current <= n:
        num = last + second_last
        yield num
        # stop at yild and when call next
        # it will start  from below to yield
        # and again yiled find resume and print in loops
        last = num
        second_last = last
        current += 1


# generte fib numbers without storing it
for val in fib(10):
    print(val)
# not storing all numbers
