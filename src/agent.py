import logging
import sys

from machine.states.runtask import RunTask

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

if __name__ == "__main__":
    first_run = True
    if first_run:
        # handle things that would happen on the first initial run
        pass
    my_state = RunTask()  # initial state
    while my_state.state != "Exit":
        my_state = my_state.on_event()
    # reached the exit state
    # let its run its state tasks
    my_state.on_event()
