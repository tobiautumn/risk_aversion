"""Compute the utility value of monetary quantities under prospect theory

"""


def power_utility_loss_aversion(z, ɣ, λ):
    """Return the utility evaluation of a monetary quantity z under power
    utility with utility curvature parameter ɣ and loss aversion
    parameter λ.

    """

    out = z ** (1 - ɣ) if z >= 0 else -λ * (-z) ** (1 - ɣ)

    return out


# Define the characteristics of the individual.
power_coefficients = [0.5, 0.5]
loss_aversion_coefficients = [2.0, 2.0]

# Define the monetary payoffs.
payoffs = [500, -550]

# Compute the utility values and print them to the screen.
out = map(
    power_utility_loss_aversion, payoffs, power_coefficients, loss_aversion_coefficients
)

for item in out:
    print(item)
