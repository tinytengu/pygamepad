"""
This example shows how to get a value of the South (A on an Xbox controler) button.
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
            print(
                "South (A) button is {}".format(
                    "pressed" if gamepad.buttons.BTN_SOUTH.value else "not pressed"
                )
            )
            time.sleep(0.01)
    except KeyboardInterrupt:
        gamepad.stop_listening()
        exit()


if __name__ == "__main__":
    main()
