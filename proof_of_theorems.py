from distributions import Normal
import math


def memoryless_property(samples, s, t):
    cnt1 = 0
    cnt2 = 0

    for x in samples:
        if x > s:
            cnt2 += 1

            if x > s + t:
                cnt1 += 1

    p1 = cnt1 / cnt2 if cnt2 != 0 else 0

    cnt3 = 0

    for x in samples:
        if x > t:
            cnt3 += 1

    p2 = cnt3 / len(samples)

    return p1, p2


def check_distribution_memoryless(samples, s, t):
    p1, p2 = memoryless_property(samples, s, t)
    diffrence = abs(p1 - p2)

    return {"P(X > s+t | X > s)": p1, "P(X > t)": p2, "Diffrence": diffrence}
