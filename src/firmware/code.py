# THIS CODE HAS NOT BEEN TESTED AND WILL MOST LIKELY NOT WORK

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.layers import Layers
from kmk.keys import KC

import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# Setup I2C
i2c = busio.I2C(scl=board.D27, sda=board.D26)
mcp = MCP23017(i2c, address=0x20)

# Define row/column pins from MCP
row_pins = [mcp.get_pin(p) for p in range(8)]
col_pins = [mcp.get_pin(p) for p in range(8, 16)]

# Set directions
for pin in row_pins:
    pin.direction = 1  # INPUT
    pin.pull = 0       # NO PULL

for pin in col_pins:
    pin.direction = 0  # OUTPUT
    pin.value = True   # Set HIGH

# Setup matrix
keyboard.matrix = MatrixScanner(
    cols=col_pins,
    rows=row_pins,
    columns_to_anodes=True,  # COL2ROW
)

# 8x8 Keymap
keyboard.keymap = [
    [
        KC.ESC,  KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7,
        KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,  KC.Y,  KC.U,
        KC.CAPS, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,  KC.H,  KC.J,
        KC.LSFT, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.N,  KC.M,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.RALT, KC.RGUI, KC.RCTL,
        KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
