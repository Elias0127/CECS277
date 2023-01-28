import abc

class PuppyState(abc.ABC):
    """ Abstract PuppyState class creates methods play() and feed() for the Concrete
    State classes to override. """

    @abc.abstractmethod
    def play(self, puppy):
        pass

    @abc.abstractmethod
    def feed(self, puppy):
        pass
