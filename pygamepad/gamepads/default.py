from inspect import getmembers
from threading import Thread

from inputs import get_gamepad

from ..buttons import GamepadButton, PressButton, RangeButton, GamepadButtons


class Gamepad:
    class Buttons(GamepadButtons):
        # Default
        BTN_NORTH = PressButton("BTN_NORTH")
        BTN_SOUTH = PressButton("BTN_SOUTH")
        BTN_EAST = PressButton("BTN_EAST")
        BTN_WEST = PressButton("BTN_WEST")
        # Start & Select
        BTN_START = PressButton("BTN_START")
        BTN_SELECT = PressButton("BTN_SELECT")
        # Thumbs
        BTN_THUMBL = PressButton("BTN_THUMBL")
        BTN_THUMBR = PressButton("BTN_THUMBR")
        # Left stick
        ABS_X = RangeButton("ABS_X")
        ABS_Y = RangeButton("ABS_Y", inversed=True)
        # Right stick
        ABS_RX = RangeButton("ABS_RX")
        ABS_RY = RangeButton("ABS_RY", inversed=True)
        # D-pad
        ABS_HAT0X = RangeButton("ABS_HAT0X", max_value=1)
        ABS_HAT0Y = RangeButton("ABS_HAT0Y", max_value=1)
        # Triggers
        ABS_Z = RangeButton("ABS_Z", max_value=2**8)
        ABS_RZ = RangeButton("ABS_RZ", max_value=2**8)
        # Bumpers
        BTN_TL = PressButton("BTN_TL")
        BTN_TR = PressButton("BTN_TR")

    class ButtonOverrides:
        """Override attributes for `Buttons` class"""

        pass

    def __init__(self):
        self.buttons = self.Buttons()
        self.overrides = self.ButtonOverrides()

        self._apply_overrides()

        self._thread = Thread(target=self._listen_handler, daemon=True)
        self._is_listening = False

    def _apply_overrides(self):
        """Apply overrides from `ButtonOverrides` subclass to `Buttons` subclass attributes"""
        overrides = getmembers(self.overrides, lambda m: isinstance(m, GamepadButton))

        for k, v in overrides:
            if not self.buttons.__getattribute__(k):
                continue
            self.buttons.__setattr__(k, v)

    @property
    def is_listening(self) -> bool:
        return self._is_listening

    def listen(self):
        self._is_listening = True
        self._thread.start()

    def stop_listening(self):
        self._is_listening = False

    def _listen_handler(self):
        while self._is_listening:
            event = get_gamepad()[0]

            # Skip Sync events
            if event.ev_type == "Sync":
                continue

            button = self.buttons.get_by_code(event.code)
            if not button:
                continue

            button.value = event.state
