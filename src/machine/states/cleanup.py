from machine.states.base import BaseState
from machine.states.wait import Wait


class CleanUp(BaseState):

    def on_event(self):
        print("hello world from clean up")
        return Wait()

