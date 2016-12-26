from evdev import uinput, ecodes as e

with uinput.UInput() as ui:
    ui.write(e.EV_KEY, e.KEY_A, 1)
    ui.write(e.EV_KEY, e.KEY_B, 1)
    ui.syn()
