import abc


class BaseState(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def on_event(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

    @property
    def state(self):
        return self.__class__.__name__
