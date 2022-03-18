"""
This example shows how to get left and right stick axis values
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
            stick_left_x = gamepad.buttons.ABS_X  # Left stick X axis
            stick_left_y = gamepad.buttons.ABS_Y  # Left stick Y axis
            axis_left = (stick_left_x.value, stick_left_y.value)

            stick_right_x = gamepad.buttons.ABS_RX  # Right stick X axis
            stick_right_y = gamepad.buttons.ABS_RY  # Right stick Y axis
            axis_right = (stick_right_x.value, stick_right_y.value)

            print(f"Left: {axis_left} | Right: {axis_right}")

            time.sleep(0.01)
    except KeyboardInterrupt:
        gamepad.stop_listening()
        exit()


if __name__ == "__main__":
    main()
