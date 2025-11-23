import numpy as np
def a():
    import numpy as np

    n = [1, 0.6]         # Numerator coefficients
    d = [1, -0.7, 0.12]  # Denominator coefficients

    # Calculate poles
    poles = np.roots(d)
    print("Poles =", poles)

    # Stability check (Z-domain: |pole| < 1)
    if all(abs(p) < 1 for p in poles):
        print("System is Stable")
    else:
        print("System is Unstable")

def b():
    import numpy as np

# Given coefficients
n = [0.5, -0.8, 0.315]
d = [1, -1.0, 0.24]

# Calculate poles
poles = np.roots(d)
print("Poles of the system =", poles)

# Stability check
stable = all(abs(p) < 1 for p in poles)

if stable:
    print("Result: The system is STABLE")
else:
    print("Result: The system is UNSTABLE")

b()