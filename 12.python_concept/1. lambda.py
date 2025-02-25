"""
Lambdas in one line anynymous functions
lambda var: ---
any thing after : is going to return

"""

func = lambda x, y, z=0: x + y + z
func = lambda x, y, z=0: print(x + y + z)
# func will store return in this case None
# func is the variable storing the functions
# we ddidnot define func like def func we just
# created anyonmous func which have no name and asign
# to func varables
print(func(1, 2, 3))
func(1, 2, 3)

# use of Lambda and its purpose
lst = [(1, 2), (-2, -4), (3, 4), (0, 0)]


# sort pairs by 2nd eleemnts
def sort_func(x):
    return x[1]


lst.sort(key=sort_func)
print(lst)

# rather than define sorting function
# above what we can do is pass a lambda
lst.sort(key=lambda x: x[1])
print(lst)

# multiication
mul = lambda x: lambda y: x * y
result = mul(2)
print(result)
# <function <lambda>.<locals>.<lambda> at 0x1050f58a0>
# call outer lambda return innder lambda take param y and mul
# and return
print(result(3))  # 6


# return function
def mul(x):
    def mul2(y):
        return x * y

    return mul2


result = mul(5)
print(result(2))
# result = mul(5)(2)
