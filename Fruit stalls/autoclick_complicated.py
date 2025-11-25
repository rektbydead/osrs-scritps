import random

from pynput.keyboard import Listener, Key
import threading
import time

from utils.autoclick_random import click
from utils.keyboard_click_random import keep_keyboard_press, keep_keyboard_release, instant_keyboard_click_with_timeout
from utils.variation_calculate import upward_variation

clicking = False
game_tick = 0.6
time_it_takes = round(game_tick * 6, 1) + 0.1

def click_loop():
    while True:
        if clicking:
            total_it_took = 0
            total_it_took += click(time_it_takes=0.075)

            # fails to open the inventory and remove the fruit
            if random.random() > 0.01:
                total_it_took += click(time_it_takes=0.075)
                # opens inventory
                total_it_took += instant_keyboard_click_with_timeout(Key.esc, base_sleep_time=game_tick, variant_sleep_time_pct=20)

                # clicks on item with left shift pressed to remove the item from inventory with 1 click
                keep_keyboard_press(Key.shift_l)
                total_it_took += click(time_it_takes=0.6, sleep_pct=100)
                keep_keyboard_release(Key.shift_l)

                # close inventory
                total_it_took += instant_keyboard_click_with_timeout(Key.esc, base_sleep_time=0.1)

            # waits for the stall to have fruit again if necessary
            if time_it_takes > total_it_took:
                remaining_sleep_time = upward_variation(time_it_takes - total_it_took, 20)
                print(f"Sleeping for {remaining_sleep_time} to wait at least for the next tick.")
                time.sleep(remaining_sleep_time)
            else:
                print("Not sleeping, it took long enough.")
        else:
            time.sleep(1)

def on_press(key):
    global clicking

    if key == Key.alt_l:
        clicking = not clicking

        if not clicking:
            print("Exiting.")
            exit(0)

        print(f"Autoclicker toggled {"ON" if clicking else "OFF"}")

    if key == Key.tab:
        print("Exiting.")
        exit(0)


# Background clicking thread
threading.Thread(target=click_loop, daemon=True).start()

with Listener(on_press=on_press) as listener:
    listener.join()