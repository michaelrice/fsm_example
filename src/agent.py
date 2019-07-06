from machine.states.runtask import RunTask


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
