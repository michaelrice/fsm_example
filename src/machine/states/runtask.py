from machine.states.base import BaseState
from machine.states.cleanup import CleanUp


class RunTask(BaseState):

    def __init__(self):
        BaseState.__init__(self)

    def on_event(self):
        print("hello world from Run Task")
        return CleanUp()
