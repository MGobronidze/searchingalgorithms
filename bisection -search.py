# Step 1: Define the function whose root you want to find
def my_function(x):
    return x**3 - 4*x - 9

# Step 2: Define the bisection_search function (as shown earlier)
def bisection_search(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b.")
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0:
            return m  # Found exact root
        elif f(a) * f(m) < 0:
            b = m  # Root is in left half
        else:
            a = m  # Root is in right half
    return (a + b) / 2  # Approximate root

# Step 3: Call the bisection_search function with the desired interval
result = bisection_search(my_function, -5, 5)

# Step 4: Print the result
print(result)
