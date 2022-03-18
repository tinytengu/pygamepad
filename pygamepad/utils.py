from time import time


def time_ms() -> int:
    """Get current UNIX timestamp in milliseconds

    :return: timestamp in ms
    :rtype: int
    """
    return round(time() * 1000)
