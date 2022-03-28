import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

wiring = {0: "p1", 2: "p2", 4: "fire",
          6: "left", 9: "down", 11: "up", 13: "right"}

names = ["p1", "p2",  "fire",
         "left",  "down", "up", "right", "0", "1", "2", "3", "4", "5", "6"]


# encoder = {}
# d0 -> 22
# d1 -> 21
# d2 -> 19
# d3 -> 28
# d4 -> 27
# d5 -> 17
# d6 -> 26

MEDIA = 1
KEY = 2
kbd = Keyboard(usb_hid.devices)
keymap = [
    Keycode.ONE,
    Keycode.TWO,
    Keycode.CONTROL,
      Keycode.LEFT_ARROW,
      Keycode.DOWN_ARROW,
      Keycode.UP_ARROW,
      Keycode.RIGHT_ARROW,
      Keycode.X,
      Keycode.Z,
]

inputs = [digitalio.DigitalInOut(board.GP0),
          digitalio.DigitalInOut(board.GP2),
          digitalio.DigitalInOut(board.GP4),
          digitalio.DigitalInOut(board.GP6),
          digitalio.DigitalInOut(board.GP9),
          digitalio.DigitalInOut(board.GP11),
          digitalio.DigitalInOut(board.GP13),

          # ANGLE ENCODER VALUES
          digitalio.DigitalInOut(board.GP22),
          digitalio.DigitalInOut(board.GP21),
          digitalio.DigitalInOut(board.GP19),
          digitalio.DigitalInOut(board.GP28),
          digitalio.DigitalInOut(board.GP27),
          digitalio.DigitalInOut(board.GP17),
          digitalio.DigitalInOut(board.GP26)
          ]

for i in range(len(inputs)):
    inputs[i].switch_to_input(pull=digitalio.Pull.UP)

last_val = 0
while True:
    # s = ""
    val = 0
    for i in range(len(inputs)-1 ,6,-1):
        val = val << 1
        if (not inputs[i].value):
            # s = s + "1"
            val = val + 1
        # else:
            # s = s + "0"
    # print(val)    x
    # print(s)
    # s = int(s)
    change = val - last_val
    print(change)
    if (abs(change) > 120):
        last_val = val
        # kbd.release_all()
        kbd.release(Keycode.Z)
        kbd.release(Keycode.X)

        continue
    elif (change > 2):
        kbd.press(Keycode.X)
        kbd.release(Keycode.Z)
    elif( change < -2):
        kbd.press(Keycode.Z)
        kbd.release(Keycode.X)
    else:
        kbd.release(Keycode.Z)
        kbd.release(Keycode.X)
    last_val = val
    for i in range(7):
        if (not inputs[i].value):
            # print(names[i])
            kbd.press(keymap[i])
        else:
            kbd.release(keymap[i])
    # print(int(s,2))
    # time.sleep(.1)
