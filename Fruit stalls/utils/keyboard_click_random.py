import time

from controllers.controllers import keyboard
from utils.variation_calculate import upward_variation


def keep_keyboard_press(key):
    keyboard.press(key)

def keep_keyboard_release(key):
    keyboard.release(key)

def instant_keyboard_click_with_timeout(key, base_sleep_time=0.05, variant_sleep_time_pct=60):
    time_to_sleep = upward_variation(base_sleep_time, variant_sleep_time_pct)
    time.sleep(time_to_sleep)

    print(f"Sleeping {time_to_sleep:.2f} seconds before pressing {key}")

    keyboard.press(key)
    keyboard.release(key)

    print(f"Pressed {key}")
    return time_to_sleep

