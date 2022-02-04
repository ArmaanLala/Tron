import board
import digitalio
import time

wiring = {0: "p1", 2: "p2", 4: "fire",
          6: "left", 9: "down", 11: "up", 13: "right"}

names = ["p1", "p2",  "fire",
         "left",  "down", "up", "right"]

inputs = [digitalio.DigitalInOut(board.GP0),
          digitalio.DigitalInOut(board.GP2),
          digitalio.DigitalInOut(board.GP4),
          digitalio.DigitalInOut(board.GP6),
          digitalio.DigitalInOut(board.GP9),
          digitalio.DigitalInOut(board.GP11),
          digitalio.DigitalInOut(board.GP13)
          ]

for i in range(len(inputs)):
    inputs[i].switch_to_input(pull=digitalio.Pull.UP)

while True:
    for i in range(len(inputs)):
        if (not inputs[i].value):
            print(names[i])
            time.sleep(1)
