from ..buttons import PressButton
from .default import Gamepad as DefaultGamepad


class Gamepad(DefaultGamepad):
    class ButtonOverrides:
        BTN_START = PressButton("BTN_SELECT")
        BTN_SELECT = PressButton("BTN_START")
