from typing import Any, Union
from inspect import getmembers

from .utils import time_ms


class GamepadButton:
    """Base gamepad button class.

    :param code: button code (name)
    :type code: str

    :param default_value: default button value
    :type default_value: Any
    """

    def __init__(self, code: str, default_value: Any = None):
        self._code = code
        self._value = default_value

    @property
    def code(self) -> str:
        return self._code

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, val) -> None:
        self._value = val

    def __repr__(self) -> str:
        return "<{}>(code={}, value={})".format(
            self.__class__.__name__, self.code, self.value
        )


class PressButton(GamepadButton):
    """Press button class.
    Represents a button which state can only be 1 (pressed) or 0 (not pressed).

    :param code: button code (name)
    :type code: str

    :param time_tolerance: pressed and released time tolerance (for `is_just_pressed` and `is_just_released` methods)
    :type time_tolerance: int
    """

    def __init__(self, code: str, time_tolerance: int = 20):
        super().__init__(code, False)

        self.time_tolerance = time_tolerance

        self._pressed_time = 0
        self._released_time = 0

    def __repr__(self):
        return "<{}>(code={}, value={}, pressed_time={}, released_time={}, is_just_pressed={}, is_just_released={})".format(
            self.__class__.__name__,
            self.code,
            self.value,
            self.pressed_time,
            self.released_time,
            self.is_just_pressed,
            self.is_just_released,
        )

    @GamepadButton.value.setter
    def value(self, value: bool) -> None:
        """Change button pressed state"""
        if self._value == value:
            return

        if value:
            self._pressed_time = time_ms()
        else:
            self._released_time = time_ms()

        self._value = bool(value)

    @property
    def pressed_time(self):
        """Get buttton pressed timestamp"""
        return self._pressed_time

    @property
    def released_time(self):
        """Get button released timestatmp"""
        return self._released_time

    @property
    def is_just_pressed(self) -> bool:
        """Is button has just been pressed.

        Checks if current timestamp and `pressed_time` difference is lower than or equals to `time_tolerance`"""
        return (time_ms() - self._pressed_time) <= self.time_tolerance and self._value

    @property
    def is_just_released(self) -> bool:
        """Is button has just been released.

        Checks if current timestamp and `released_time` difference is lower than or equals to `time_tolerance`"""
        return (
            time_ms() - self._released_time
        ) <= self.time_tolerance and not self._value


class RangeButton(GamepadButton):
    """Press button class.
    Represents a button which state can between some range of values (0-1, -1-1, etc.).

    :param code: button code (name)
    :type code: str

    :param max_value: max button value (for normalizing)
    :type max_value: int

    :param inversed: should value be inversed
    :type inversed: bool
    """

    def __init__(
        self, code: str, max_value: int = 2**15, inversed: bool = False
    ) -> None:
        super().__init__(code, 0.0)

        self.max_value = max_value
        self.inversed = inversed

    @GamepadButton.value.setter
    def value(self, val: int) -> None:
        self._value = round(val / self.max_value, 6)
        if self.inversed:
            self._value = -self._value


class GamepadButtons:
    """Gamepad buttons collection class"""

    def get_by_code(self, code: str) -> Union[GamepadButton, None]:
        """Returns class attribute that contains `GamepadButtons` instance as its value and has matching `code` property

        :param code: `GamepadButtons` instance code value
        :type code: str

        :return: according `GamepadButtons` class instance
        :rtype: Union[GamepadButton, None]
        """
        for k, v in self.get_list():
            if v.code == code:
                return self.__getattribute__(k)
        return None

    def get_list(self) -> tuple[str, GamepadButton]:
        """Returns class attributes that contain `GamepadButtons` instance as its value"""
        return getmembers(self, lambda a: isinstance(a, GamepadButton))
