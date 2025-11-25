import random


def upward_variation(base, pct):
    max_extra = base * (pct / 100.0)
    extra = random.uniform(0, max_extra)
    return base + extra
