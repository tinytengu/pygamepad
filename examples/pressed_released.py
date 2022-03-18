"""
This example shows how to check if a button has just been pressed
and/or released, so you don't need to write your own conditions and etc.
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
            button = (
                gamepad.buttons.BTN_THUMBR
            )  # Right thumb button (when you press on the right stick)

            if button.is_just_pressed:
                print("Right thumb button has just been pressed")
            if button.is_just_released:
                print("Right thumb button has just been released")
                print(
                    "The button was pressed for {} ms.".format(
                        button.released_time - button.pressed_time
                    )
                )
            time.sleep(0.01)
    except KeyboardInterrupt:
        gamepad.stop_listening()
        exit()


if __name__ == "__main__":
    main()
