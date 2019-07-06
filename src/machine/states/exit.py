from machine.states.base import BaseState


class Exit(BaseState):
    def on_event(self):
        print("Doing some state cleanup before we exit")
        raise SystemExit
