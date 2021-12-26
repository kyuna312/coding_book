import abc


class Abstraction:
    """
    Define the abstraction's interface.
    Maintain a reference to an object of type Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def operation(self):
        self._imp.operation_imp()


class Implementor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def operation_imp(self):
        pass


class ConcreteImplementorA(Implementor):

    def operation_imp(self):
        pass


class ConcreteImplementorB(Implementor):

    def operation_imp(self):
        pass


def main():
    concrete_implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(concrete_implementor_a)
    abstraction.operation()


if __name__ == "__main__":
    main()