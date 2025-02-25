"""
Ability to Implements to custom Logic
on our own class

"""


class Page:
    def __init__(self, word, page_number):
        self.words = word
        self.page_number = page_number

    # overload addition operation
    def __add__(self, other):
        print("Hello")
        new_words = self.words + other.words
        # increemnt page number
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)


page1 = Page(" this is a grate", 1)
page2 = Page(" this is a grate", 2)
# page1 + page2 --> give page3
page3 = page1 + page2
print(page3.words, page3.page_number)
