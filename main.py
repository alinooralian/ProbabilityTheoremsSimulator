from random_number_generator import (
    LinearCongruentialGenerator,
    XorShift,
    compare_engines,
)
import distributions as dist
import analysis
import proof_of_theorems
import sys
import os
from time import sleep


def clean(t=0):
    sleep(t)
    os.system("cls")


def menu(options, title=""):
    print(title)

    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    print("-" * 50)

    while True:
        try:
            choice = input("Your Choice:\t")
            choice = int(choice)

            if 1 <= choice <= len(options):
                return choice
            print("Your input is invalid!")
        except:
            print("Your input is invalid!")


def read_int(prompt):
    while True:
        try:
            k = int(input(prompt))
            return k
        except:
            print("Your input is invalid!")


def read_float(prompt):
    while True:
        try:
            k = float(input(prompt))
            return k
        except:
            print("ERROR: Your input is invalid!")


def print_report(dist_name, params, M, samples, distribution):
    report = analysis.build_report(dist_name, params, M, samples, distribution)

    for key, val in report.items():
        print(f"{key}: {val}")

    input("\n\nPress ENTER to return...")


while True:
    clean()

    print("=" * 10, "Probability theorems simulator and prover", "=" * 10)

    choice = menu(
        [
            "Phase 0: Comparison of random number generation engines(LCG Vs XorShift)",
            "Phase 1 & 2: Distribution simulation and statistical analysis",
            "Phase 3: Examining the memoryless property(Geometry / Exponential)",
            "Pahse 3: Examining Limit Approximation Theorems(Normal instead of Binomial / Poisson)",
            "Exit",
        ]
    )

    clean()

    if choice == 1:
        simple_size = read_int("Enter Your Number:\t")
        
        clean()

        compare_engines(simple_size)

        input("\n\nPress ENTER to return...")
    elif choice == 2:
        choice = menu(
            ["LCG (Linear Congruential Generator)", "XorShift"],
            "Choosing a random number generator:",
        )

        clean()

        if choice == 1:
            engine = LinearCongruentialGenerator()
        else:
            engine = XorShift()

        choice = menu(
            ["Bernoulli", "Binomial", "Geometric", "Normal", "Poisson", "Exponential"],
            "Choosing a distribution:",
        )

        clean()

        if choice == 1:
            while True:
                try:
                    p = read_float("Enter the probability of success(p):\t")
                    distribution = dist.Bernoulli(engine, p)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated(must be greater than 1):\t"
            )

            clean()

            samples = analysis.genrete_samples(distribution, M)

            print_report("Bernoulli", f"P = {p}", M, samples, distribution)
        elif choice == 2:
            while True:
                try:
                    n = read_int(
                        "Enter the number of times to repeat the experiment(n):\t"
                    )
                    p = read_float("Enter the probability of success(p):\t")
                    distribution = dist.Binomial(engine, n, p)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated(must be greater than 1)(M):\t"
            )

            clean()

            samples = analysis.genrete_samples(distribution, M)

            print_report("Binomial", f"P = {p}, N = {n}", M, samples, distribution)

        elif choice == 3:
            while True:
                try:
                    p = read_float("Enter the probability of success:(p)\t")
                    distribution = dist.Geometric(engine, p)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated(must be greater than 1):\t"
            )

            clean()

            samples = analysis.genrete_samples(distribution, M)

            print_report("Geometric", f"P = {p}", M, samples, distribution)
        elif choice == 4:
            mu = read_float("Enter the mean parameter(μ):\t")

            while True:
                try:
                    sigma = read_float("Enter the standard deviation parameter(σ):\t")
                    distribution = dist.Normal(engine, mu, sigma)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated(must be greater than 1):\t"
            )

            clean()

            samples = analysis.genrete_samples(distribution, M)

            print_report("Normal", f"μ = {mu}, σ = {sigma}", M, samples, distribution)
        elif choice == 5:
            while True:
                try:
                    lam = read_float("Enter the lambda parameter(λ):\t")
                    distribution = dist.Poisson(engine, lam)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated(must be greater than 1):\t"
            )

            clean()

            samples = analysis.genrete_samples(distribution, M)

            print_report("Poisson", f"λ = {lam}", M, samples, distribution)
        else:
            while True:
                try:
                    lam = read_float("Enter the lambda parameter(λ):\t")
                    distribution = dist.Exponential(engine, lam)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated (must be greater than 1):\t"
            )

            clean()

            samples = analysis.genrete_samples(distribution, M)

            print_report("Exponential", f"λ = {lam}", M, samples, distribution)
    elif choice == 3:
        choice = menu(
            ["LCG (Linear Congruential Generator)", "XorShift"],
            "Choosing a random number generator:",
        )

        clean()

        if choice == 1:
            engine = LinearCongruentialGenerator()
        else:
            engine = XorShift()

        choice = menu(["Geometric", "Exponential"], "Select the desired distribution:")

        clean()

        if choice == 1:
            while True:
                try:
                    p = read_float("Enter the probability of success(p):\t")
                    distribution = dist.Geometric(engine, p)
                    break
                except ValueError as e:
                    print(e)
        else:
            while True:
                try:
                    lam = read_float("Enter the lambda parameter(λ):\t")
                    distribution = dist.Exponential(engine, lam)
                    break
                except ValueError as e:
                    print(e)

        M = read_int(
            "Enter the number of times the sample will be generated (must be greater than 1):\t"
        )
        s = read_int("Enter s:\t")
        t = read_int("Enter t:\t")

        clean()

        samples = analysis.genrete_samples(distribution, M)
        result = proof_of_theorems.check_distribution_memoryless(samples, s, t)

        for key, val in result.items():
            print(f"{key} = {val}")

        input("\n\nPress ENTER to return...")
    elif choice == 4:
        choice = menu(
            ["LCG (Linear Congruential Generator)", "XorShift"],
            "Choosing a random number generator:",
        )

        clean()

        if choice == 1:
            engine = LinearCongruentialGenerator()
        else:
            engine = XorShift()

        choice = menu(
            [
                "Binomial approximation by normal(n >= 50)",
                "Poisson approximation by normal(λ >= 30)",
            ],
            "Choose the desired limit theorem:",
        )

        clean()

        if choice == 1:
            while True:
                try:
                    n = read_int(
                        "Enter the number of times to repeat the experiment(n >= 50):\t"
                    )
                    p = read_float("Enter the probability of success(p):\t")
                    distribution = dist.Binomial(engine, n, p)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated(must be greater than 1)(M):\t"
            )
            a = read_int("Enter the lower limit:\t")
            b = read_int("Enter the upper limit:\t")

            clean()

            samples = analysis.genrete_samples(distribution, M)

            result = proof_of_theorems.binomial_normal_approximation(
                samples, n, p, a, b
            )

            for key, val in result.items():
                print(f"{key} = {val}")

            input("\n\nPress ENTER to return...")
        else:
            while True:
                try:
                    lam = read_float("Enter the lambda parameter(λ):\t")
                    distribution = dist.Poisson(engine, lam)
                    break
                except ValueError as e:
                    print(e)

            M = read_int(
                "Enter the number of times the sample will be generated (must be greater than 1)(M):\t"
            )
            a = read_int("Enter the lower limit:\t")
            b = read_int("Enter the upper limit:\t")

            clean()

            samples = analysis.genrete_samples(distribution, M)

            result = proof_of_theorems.poisson_normal_approximation(samples, lam, a, b)

            for key, val in result.items():
                print(f"{key} = {val}")

            input("\n\nPress ENTER to return...")
    else:
        sys.exit(0)
