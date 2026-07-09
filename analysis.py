from distributions import BaseDistribution


def genrete_samples(distributions: BaseDistribution, M):
    samples = []

    for _ in range(M):
        samples.append(distributions.generate_sample())

    return samples


def empirical_mean(samples):
    ans = 0

    for x in samples:
        ans += x

    return ans / len(samples)


def empirical_variance(samples):
    mean = empirical_mean(samples)
    ans = 0

    for x in samples:
        ans += (x - mean) ** 2

    return ans / (len(samples) - 1)


def percent_error(theorical, empirical):
    return abs((theorical - empirical) / theorical) * 100
