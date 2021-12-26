import abc


class Target(metaclass=abc.ABCMeta):

    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):

    def request(self):
        self._adaptee.specific_request()


class Adaptee:


    def specific_request(self):
        pass


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()