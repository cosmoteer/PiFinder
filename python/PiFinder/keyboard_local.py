import enum
from time import sleep
from PiFinder.keyboard_interface import KeyboardInterface
from enum import Enum
import logging
from curtsies import Input

from PyHotKey import Key, keyboard_manager as manager


class KeyboardLocal(KeyboardInterface):
    NA = 10
    UP = 11
    DN = 12
    ENT = 13
    A = 20
    B = 21
    C = 22
    D = 24
    ALT_UP = 101
    ALT_DN = 102
    ALT_A = 103
    ALT_B = 104
    ALT_C = 105
    ALT_D = 106
    ALT_0 = 110
    LNG_A = 200
    LNG_B = 201
    LNG_C = 202
    LNG_D = 203
    LNG_ENT = 204

    def __init__(self, q):
        self.q = q
        manager.set_wetkey_on_release(Key.enter, self.callback, self.B)
        manager.set_wetkey_on_release(Key.up, self.callback, self.B)
        manager.set_wetkey_on_release(Key.down, self.callback, self.B)
        manager.set_wetkey_on_release('a', self.callback, self.A)
        manager.set_wetkey_on_release('b', self.callback, self.B)
        manager.set_wetkey_on_release('c', self.callback, self.C)
        manager.set_wetkey_on_release('d', self.callback, self.D)
        manager.set_wetkey_on_release('0', self.callback, 0)
        manager.set_wetkey_on_release('1', self.callback, 1)
        manager.set_wetkey_on_release('2', self.callback, 2)
        manager.set_wetkey_on_release('3', self.callback, 3)
        manager.set_wetkey_on_release('4', self.callback, 4)
        manager.set_wetkey_on_release('5', self.callback, 5)
        manager.set_wetkey_on_release('6', self.callback, 6)
        manager.set_wetkey_on_release('7', self.callback, 7)
        manager.set_wetkey_on_release('8', self.callback, 8)
        manager.set_wetkey_on_release('9', self.callback, 9)
        manager.register_hotkey([Key.enter, Key.up], None, self.callback, self.ALT_UP)
        manager.register_hotkey([Key.enter, Key.down], None, self.callback, self.ALT_DN)
        manager.register_hotkey([Key.enter, 'a'], None, self.callback, self.ALT_A)
        manager.register_hotkey([Key.enter, 'b'], None, self.callback, self.ALT_B)
        manager.register_hotkey([Key.enter, 'c'], None, self.callback, self.ALT_C)
        manager.register_hotkey([Key.enter, 'd'], None, self.callback, self.ALT_D)
        manager.register_hotkey([Key.enter, '0'], None, self.callback, self.ALT_0)
        manager.register_hotkey([Key.shift, 'a'], None, self.callback, self.LNG_A)
        manager.register_hotkey([Key.shift, 'b'], None, self.callback, self.LNG_B)
        manager.register_hotkey([Key.shift, 'c'], None, self.callback, self.LNG_C)
        manager.register_hotkey([Key.shift, 'd'], None, self.callback, self.LNG_D)
        manager.register_hotkey([Key.shift, Key.enter], None, self.callback, self.LNG_ENT)
        # manager.logger = True

    def callback(self, key):
        print(f"Got key: {key}")
        self.q.put(key)

    def run_keyboard(self, q, script_path=None):
        print("Ready for keyboard input")
        while True:
            try:
                res = getch()
                print(f"Got input: {res}")
                q.put(res)
            except Exception as e:
                print(f"Keyboard input failed with exception: {e}")
                pass
