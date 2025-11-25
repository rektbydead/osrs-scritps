import time

from pynput.keyboard import Listener, Key
import threading

from controllers.controllers import keyboard
from utils.variation_calculate import upward_variation

clicking = False
game_tick = 0.6
time_it_takes = round(game_tick * 6, 1) + 0.1

def click_loop():
    while True:
        if clicking:
            keyboard.press(Key.shift_l)
            keyboard.press(Key.esc)

            sleepy_time = upward_variation(base=0.005, pct=500)
            print(f"Sleeping for {sleepy_time:.5f} seconds before clicking")
            time.sleep(sleepy_time)
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