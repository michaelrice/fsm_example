import time
from machine.states.base import BaseState
from machine.states.exit import Exit


class Wait(BaseState):
    def on_event(self):
        print("Waiting")
        # implement some kind of
        # waiting logic
        time.sleep(5)
        print("Still sleeping")
        time.sleep(5)
        return Exit()

