import random

from pynput.mouse import Button
import time

from controllers.controllers import mouse
from utils.variation_calculate import upward_variation

def weighted_clicks():
    weights = {
        #0: 10,
        1: 100,
        # 2: 4,
        # 3: 3,
        # 4: 2.91,
        # 5: 0.09
    }

    population = list(weights.keys())
    probs = list(weights.values())

    return random.choices(population, probs)[0]


def click(time_it_takes, click_base=0.150, click_pct=40, sleep_pct=20):
    num_clicks = weighted_clicks()
    # click_time_variations = [upward_variation(click_base, click_pct) for _ in range(num_clicks - 1)] if num_clicks > 1 else []
    sleep_time = upward_variation(time_it_takes, sleep_pct)

    print(f"Sleeping for {sleep_time:.2f} seconds (default: {time_it_takes}) before clicking")
    time.sleep(sleep_time)

    for i in range(num_clicks):
        mouse.click(Button.left)

        # if len(click_time_variations) > 1 and i < len(click_time_variations):
        #     time.sleep(click_time_variations[i])

    # if len(click_time_variations) > 1:
    #     print(f"Clicked {num_clicks} times ({", ".join(f"{v:.2f}" for v in click_time_variations)})")
    # else:
    print(f"Clicking {num_clicks} time")

    return sleep_time


def randomClicksPerSecond(min, max):
    num_clicks = random.randint(min, max)

    total_window = random.uniform(0.5, 1.4)
    random_parts = [random.uniform(0.05, 0.45) for _ in range(num_clicks)]
    total_random = sum(random_parts)
    scale = total_window / total_random
    delays = [(p * scale) + random.uniform(-0.01, 0.03) for p in random_parts]

    for d in delays:
        mouse.click(Button.left)
        time.sleep(d)