import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D9, board.D10, board.D11)
keyboard.row_pins = (board.D12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.LCMD(KC.C),
        KC.LCMD(KC.V), 
        KC.MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()