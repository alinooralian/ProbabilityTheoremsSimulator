# 🎲 Probability Simulation & Statistical Analysis

A Python implementation of pseudo-random number generators, probability distributions, and statistical simulations without using external random or statistical libraries.

This project was developed as part of a **Probability and Statistics** course to demonstrate how random number generation, probability distributions, and statistical analysis can be implemented from scratch.

---

## 📌 Project Objectives

The main goals of this project are:

- Implement pseudo-random number generators from scratch.
- Generate samples from common probability distributions.
- Compare empirical statistics with theoretical values.
- Verify important probabilistic properties through simulation.
- Demonstrate the Normal approximation for Binomial and Poisson distributions.

---

## 🚫 Restrictions

The following libraries are **NOT** used for random number generation or probability distributions:

- NumPy
- SciPy
- random

Only Python's standard libraries (such as `math` and `time`) are used.

---

# 📂 Project Structure

```
project/
│
├── generators/
│   ├── lcg.py
│   └── xorshift.py
│
├── distributions/
│   ├── bernoulli.py
│   ├── binomial.py
│   ├── geometric.py
│   ├── poisson.py
│   ├── exponential.py
│   └── normal.py
│
├── statistics/
│   ├── analysis.py
│   └── approximation.py
│
├── main.py
└── README.md
```

---

# ⚙️ Phase 1 — Random Number Generators

Two pseudo-random number generators are implemented.

## Linear Congruential Generator (LCG)

Formula:

\[
X_{n+1}=48271X_n \mod (2^{31}-1)
\]

Output:

\[
U_n=\frac{X_n}{2^{31}-1}
\]

---

## XorShift (32-bit)

Implemented using the classical 32-bit XorShift algorithm.

```python
x ^= (x << 13)
x ^= (x >> 17)
x ^= (x << 5)
```

Both generators are benchmarked by generating one million random numbers.

---

# 🎯 Phase 2 — Probability Distributions

The following distributions are implemented using the custom random generators.

| Distribution | Sampling Method |
|--------------|----------------|
| Bernoulli | Uniform comparison |
| Binomial | Sum of Bernoulli trials |
| Geometric | Repeated Bernoulli trials |
| Poisson | Knuth algorithm |
| Exponential | Inverse Transform Sampling |
| Normal | Box–Muller Transform |

---

# 📊 Phase 3 — Statistical Analysis

For each distribution:

- Generate a large number of samples.
- Compute the empirical mean.
- Compute the empirical variance.
- Compare empirical values with theoretical values.
- Calculate percentage error.

---

# 🔬 Phase 4 — Probability Experiments

## Memoryless Property

Verified experimentally for:

- Geometric Distribution
- Exponential Distribution

The following identity is tested:

\[
P(X>s+t \mid X>s)=P(X>t)
\]

---

## Normal Approximation

Normal approximation is verified for:

- Binomial Distribution
- Poisson Distribution

The approximation uses **Continuity Correction** when required.

---

# 📈 Implemented Algorithms

- Linear Congruential Generator (LCG)
- XorShift RNG
- Bernoulli Sampling
- Binomial Sampling
- Geometric Sampling
- Knuth Poisson Generator
- Inverse Transform Sampling
- Box–Muller Transform
- Empirical Mean
- Empirical Variance
- Percentage Error
- Normal Approximation
- Memoryless Property Verification

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/your-username/Probability-Simulation.git
```

Enter the project directory:

```bash
cd Probability-Simulation
```

Run:

```bash
python main.py
```

---

# 📚 Concepts Covered

- Pseudo-Random Number Generation
- Probability Distributions
- Monte Carlo Simulation
- Statistical Inference
- Normal Approximation
- Memoryless Property
- Empirical vs Theoretical Analysis

---

# 🛠️ Built With

- Python 3
- math
- time

---

# 👨‍💻 Author

**Ali Nooralian**

Computer Science Student

---

# 📄 License

This project is intended for educational purposes.