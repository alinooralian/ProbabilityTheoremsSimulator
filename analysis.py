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


def build_report(dist_name, params, M, samples, distribution):
    mean_emp = empirical_mean(samples)
    var_emp = empirical_variance(samples)
    mean_theo = distribution.theoretical_mean()
    var_theo = distribution.theoretical_variance()
    err_mean = percent_error(mean_theo, mean_emp)
    err_var = percent_error(var_theo, var_emp)

    return {
        "Distribution name": dist_name,
        "Params": params,
        "M": M,
        "Mean empirical": mean_emp,
        "Variance empirical": var_emp,
        "Mean theoretical": mean_theo,
        "Variance theoretical": var_theo,
        "Error mean percent": err_mean,
        "Error variance percent": err_var,
    }
