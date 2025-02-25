"""

"""


def count_to(count):
    """Our iterator impelemnation"""
    # our list
    numbers_in_germans = ["eins", "zwei", "drei", "vier", "funf"]
    # our bilt in itertaors
    # create a tuples such as (1, "eins")
    # range importants to what we have to count
    iterator = zip(range(count), numbers_in_germans)
    # iterate through our Iterable List
    # Extract the german Numbers
    # Put them in a generator called number
    for position, number in iterator:
        # return a 'generator' contaning the number in German
        yield number


# let's test the generator returned by our iterator
for num in count_to(4):
    print("{}".format(num))
"""
It provides its own built in iterators which make easier to develop
customized iterator
"""
