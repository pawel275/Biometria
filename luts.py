import math


def zero():
    return 256 * [0]


def log(k):
    return _normalized([math.log(i, k) - 1 for i in range(256)])


def exp(k):
    return _normalized([i ** k for i in range(256)])


def hist_stretch(a, b):
    if a > b:
        a, b = b, a
    return [int(min(255, max(0, (255 / (b - a)) * (i - a)))) for i in range(256)]


def hist_eq(color):
    d = 256 * [0]
    for x in color:
        d[x] += 1
    for i in range(255):
        d[i + 1] += d[i]
    d0 = next(x for x in d if x != 0)
    return [int(255 * (d[i] - d0) / (len(color) - d0)) for i in range(256)]


def threshold(t):
    return [0 if i < t else 255 for i in range(256)]


def _normalized(lut):
    scale = 255 / max(lut)
    return list(map(lambda x: int(min(255, x * scale)), lut))

