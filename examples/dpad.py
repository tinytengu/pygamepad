"""
The D-pad works in the same way as the sticks,
the values are also represented as two axes,
the only difference is that the d-pad can have 1, 0 and -1, without intermediate values.
"""

import time
from pygamepad.gamepads.default import Gamepad


def main():
    # Create gamepad instance
    gamepad = Gamepad()
    # And begin listening for buttons events in separated thread
    gamepad.listen()

    try:
        # Repeatedly output some info, you don't have to use some..
        # infinite loops or so, this is just an example, put it wherever
        # you wish unless it's working
        while True:
            dpad_x = gamepad.buttons.ABS_HAT0X  # D-pad X axis
            dpad_y = gamepad.buttons.ABS_HAT0Y  # D-pad Y axis

            print("D-pad axes: ({}, {})".format(dpad_x.value, dpad_y.value))

            time.sleep(0.01)
    except KeyboardInterrupt:
        gamepad.stop_listening()
        exit()


if __name__ == "__main__":
    main()
