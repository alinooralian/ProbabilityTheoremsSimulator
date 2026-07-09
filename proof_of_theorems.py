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


def empirical_range_probability(samples, a, b):
    cnt = 0

    for x in samples:
        if a <= x <= b:
            cnt += 1

    return cnt / len(samples)


def normal_range_probability_with_continuity(mu, sigma, a, b):
    z_upper = (b + 0.5 - mu) / sigma
    z_lower = (a - 0.5 - mu) / sigma

    return Normal.standard_cdf(z_upper) - Normal.standard_cdf(z_lower)


def binomial_normal_approximation(samples, n, p, a, b):
    p_empirical = empirical_range_probability(samples, a, b)

    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    p_normal = normal_range_probability_with_continuity(mu, sigma, a, b)

    difference = abs(p_empirical - p_normal)

    return {"Probability Empirical": p_empirical, "Probablity Normal": p_normal, "Difference": difference}

