from ..buttons import PressButton
from .default import Gamepad


class DefenderGamepad(Gamepad):
    class ButtonOverrides:
        BTN_START = PressButton("BTN_SELECT")
        BTN_SELECT = PressButton("BTN_START")
