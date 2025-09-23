class ValueHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

x = 15
try:
    if x > 10:
        raise ValueHighError("Value is too high", x)
except ValueHighError as e:
    print(e.message, e.value)