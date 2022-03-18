"""
Let's use Defender X7 gamepad config
"""

import time
from pygamepad.gamepads.defenderx7 import Gamepad


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
            select_button = gamepad.buttons.BTN_SELECT
            start_button = gamepad.buttons.BTN_START

            if select_button.is_just_pressed:
                print("You just pressed Select button")

            if start_button.is_just_pressed:
                print("You just pressed Start button")

            time.sleep(0.01)
    except KeyboardInterrupt:
        gamepad.stop_listening()
        exit()


if __name__ == "__main__":
    main()
