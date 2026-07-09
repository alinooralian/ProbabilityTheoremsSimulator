from distributions import BaseDistribution


def genrete_samples(distributions: BaseDistribution, M):
    samples = []

    for _ in range(M):
        samples.append(distributions.generate_sample())

    return samples
