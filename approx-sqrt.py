def sqrt(x):

    z = 1.0

#Keep getting a better estiate for the square root until you are within 2 decimal places
    while abs(z*z- x) >= 0.0000001:
        # Get a better approx for the square root
        z -= (z*z - x) / (2*z)

    return z

z = sqrt(64.0)

print(z)

print(z*z)