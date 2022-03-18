# py_gamepad 

## Python 3 module that allows you to control your gamepad

> Supports Python 3 only, becaus of typehintings and some other cool Python 3 things.
>
>**3.4+ actually, anyway, 3.10 is out, there's literally no reason to use the old versions-*

## Usage
Since I needed to use this thing in my project with some UI and.. things, I've designed it with multithreading support (actually, this is the only option lol) so no need to worry for this, just import needed gamepad, fire `listen` method and you are good to go.

Here's an example:
```python
# main.py

from time import sleep

from pygamepad.gamepads import Gamepad


def main():
    gamepad = Gamepad()
    gamepad.listen()  # And that's it

    # Now you can read gamepad values in the main thread
    try:
        while True:
            print("START button value:", gamepad.buttons.BTN_START.value)
            sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        # Kill gamepad's listening thread
        gamepad.stop_listening()
        # And exit from the program
        exit()


if __name__ == "__main__":
    main()
```

## Q&A
***Ok, how do I know without opening whole module script which gamepad buttons I can use?***<br>
Since module uses typehinting literally everywhere you just can write `gamepad.buttons` and autocomplete will show you all of existing buttons.
Alternatively you may just open Gamepad class and see all the button in its `Buttons` subclass.
<details>
    <summary>Screenshots</summary>
    <img src="https://i.imgur.com/WaKjR3x.png" alt="Autocompletion"/>
    <img src="https://i.imgur.com/Oq0pEi4.png" alt="Autocompletion"/>
</details>
<hr>

***What gamepads does it support?***
Defender X7 and Xbox 360 for sure. Well, I only own Defender X7 gamepad so I tested it in x-input mode so there's no gyroscope and touch capabilities, BUT you can contribute your changes :)

Since people may use like any kind of gamepads (Chinese especially) it may not work out of the box or some buttons may be swapped and etc., in that case you can inherit from default gamepad class (`pygamepad.gamepads.default.Gamepad`) and alter some things for your case.
I had to do so for my Defender X7 gamepad because Start and Select buttons were swapped for some reason (it uses `inputs` module under the hood and for some reason `0x13a` and `0x13b` buttons are swapped or idk), so I changed Start to Select and Select to Start using special `ButtonOverrides` subclass where you can.. well.. you've guessed it, override default button mappings:

```python
# pygamepad/gamepads/defenderx7.py

from gamepad.buttons import PressButton
from .default import Gamepad


class DefenderGamepad(Gamepad):
    class ButtonOverrides:
        BTN_START = PressButton("BTN_SELECT")
        BTN_SELECT = PressButton("BTN_START")
```
