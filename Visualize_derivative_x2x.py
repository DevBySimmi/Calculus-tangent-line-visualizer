# Visualize derivatives in Python

import numpy as np
import matplotlib.pyplot as plt

# Define the function
def expr(x):
    return x**2

# Define the derivative
def expr_der(x):
    return 2*x

# Values for plotting
values = np.linspace(-10, 10, 500)

# Point of tangency
x1 = -5
y1 = expr(x1)
slope = expr_der(x1)

# Tangent line equation
def line(x, x1, y1):
    return slope * (x - x1) + y1

# Create figure
plt.figure(figsize=(12, 7))

# Plot function
plt.plot(values, expr(values),
         linewidth=3,
         label='f(x) = x²')

# Shade area under curve
plt.fill_between(
    values,
    expr(values),
    alpha=0.15,
    label='Area under curve'
)

# Plot tangent line
xrange = np.linspace(x1-5, x1+5, 100)
plt.plot(
    xrange,
    line(xrange, x1, y1),
    '--',
    linewidth=2.5,
    label=f'Tangent at x = {x1}'
)

# Point of tangency
plt.scatter(
    x1,
    y1,
    s=200,
    color='red',
    zorder=5
)

# Annotate point
plt.annotate(
    f'({x1}, {y1})',
    xy=(x1, y1),
    xytext=(-7, 35),
    arrowprops=dict(arrowstyle='->')
)

# Show slope
plt.text(
    3,
    80,
    f"Slope = {slope}",
    fontsize=12,
    bbox=dict(facecolor='white')
)

# Show tangent equation
intercept = y1 - slope*x1
plt.text(
    3,
    70,
    f"Tangent: y = {slope}x + {intercept}",
    fontsize=12,
    bbox=dict(facecolor='white')
)

# Show derivative
plt.text(
    3,
    60,
    f"f'({x1}) = {slope}",
    fontsize=12,
    bbox=dict(facecolor='white')
)

# Axes
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

# Labels
plt.xlabel('x', fontsize=13)
plt.ylabel('y', fontsize=13)
plt.title(
    'Function, Derivative and Tangent Line',
    fontsize=18
)

plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)

plt.xlim(-11, 11)
plt.ylim(-30, 110)

plt.show()

# Information
print("="*40)
print("FUNCTION ANALYSIS")
print("="*40)
print(f"Function:      f(x) = x²")
print(f"Derivative:    f'(x) = 2x")
print(f"Point:         ({x1}, {y1})")
print(f"Slope:         {slope}")
print(f"Tangent line:  y = {slope}x + {intercept}")
print("="*40)