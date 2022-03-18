"""
This is not much different from the example with sticks,
the values are still normalized,
so you will get uniform values for both sticks and triggers.
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
            left_trigger = gamepad.buttons.ABS_Z
            right_trigger = gamepad.buttons.ABS_RZ

            print(
                "Left: {} | Right: {}".format(left_trigger.value, right_trigger.value)
            )

            time.sleep(0.01)
    except KeyboardInterrupt:
        gamepad.stop_listening()
        exit()


if __name__ == "__main__":
    main()
