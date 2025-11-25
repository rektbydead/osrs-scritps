import time

from pynput.keyboard import Listener, Key
import threading

from controllers.controllers import keyboard

clicking = False
game_tick = 0.6
time_it_takes = round(game_tick * 6, 1) + 0.1

def click_loop():
    while True:
        if clicking:
            keyboard.press(Key.shift_l)
            keyboard.press(Key.esc)
            time.sleep(0.005)
        else:
            time.sleep(1)


def on_press(key):
    global clicking

    if key == Key.alt_l:
        clicking = not clicking
        keyboard.release(Key.shift_l)
        keyboard.release(Key.esc)
        print(f"Autoclicker toggled {"ON" if clicking else "OFF"}")

    if key == Key.tab:
        print("Exiting.")
        exit(0)


# Background clicking thread
threading.Thread(target=click_loop, daemon=True).start()

with Listener(on_press=on_press) as listener:
    listener.join()