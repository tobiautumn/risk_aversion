"""Compute the utility value of monetary quantities under prospect theory

"""


def power_utility_loss_aversion(z_list, gamma, lambda_):
    """Return the utility evaluation of a vector of monetary
    quantities *z* under power utility with utility curvature
    parameter *gamma* and loss aversion parameter *lambda_*.

    """

    out = z_list
    for i, z in enumerate(z_list):
        if z >= 0:
            out[i] = z ** (1 - gamma)
        else:
            out[i] = -lambda_ * (-z) ** (1 - gamma)

    return out


# Define the characteristics of the individual.
power_coefficient = 0.5
loss_aversion_coefficient = 2.0

# Define the monetary payoffs.
payoffs = [500, -550]

# Compute the utility values
evaluations = power_utility_loss_aversion(
    payoffs, power_coefficient, loss_aversion_coefficient
)

# Print the utility values to the screen.
print(evaluations)

# Goal: Understand what happened here.
print(payoffs)
