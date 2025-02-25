class Command:
    # served as interface
    def execute(self):
        pass


# define concrete command operations
class Copy(Command):
    def execute(self):
        print("Copying...")


class Paste(Command):
    def execute(self):
        print("pasting...")


class Save(Command):
    def execute(self):
        print("Saving...")


# invoker class create multiple
# concrete command objects and store them in a List
# we called this invoker class Macro here because it simulates
# how micor works in a word processor
# store sequence of actions taken in a single container
# so that user doesnot have to execute the actions individually
# triggered them with one step process like clicking on Macro buttons
class Macro:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for o in self.commands:
            o.execute()


macro = Macro()
macro.add(Copy())
macro.add(Paste())
macro.add(Save())
macro.run()
