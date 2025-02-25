from abc import ABC, abstractmethod


class AbstarctExpression(ABC):
    # force to be overidden
    @abstractmethod
    def interprete(self):
        pass


class NonterminalExpression(AbstarctExpression):
    def __init__(self, expression):
        self._expression = expression

    def interprete(self):
        print("Non terminal expression being interpreted...")
        self._expression.interprete()


class TerminalExpression(AbstarctExpression):

    def interprete(self):
        print("terminal expression being interpreted...")


ast = NonterminalExpression(NonterminalExpression(TerminalExpression()))
ast.interprete()
