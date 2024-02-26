# Collaborated with Marlesha Ellis, we didnt go back and forth over github but sent our pycharm files back and forth
# over the Discord App these are the final outcomes of our work
# I(Austin) Did the initial draft and then sent it too marlesha too go over and check my code and give me feedback on
# how too improve it.
import numpy as np    # used for linspace (even distribution)
import matplotlib.pyplot as plt  # used for plotting
from scipy import stats   #using stats norm cdf and pdf to find probability and cumulative distributions

# Part 1
# Generate a range of values for x
x_values = np.linspace(-3, 3, 1000)

# Compute the probability density function (pdf) for N(0, 1)
pdf_values = stats.norm.pdf(x_values, loc=0, scale=1)

# Compute the cumulative distribution function (cdf) for N(0, 1)
cdf_values = stats.norm.cdf(x_values, loc=0, scale=1)

# Find the probability P(x < 1)
probability_x_less_than_1 = stats.norm.cdf(1, loc=0, scale=1)

# Plot the PDF with shaded area
plt.figure(figsize=(10, 5))
plt.plot(x_values, pdf_values, label='PDF')
plt.fill_between(x_values, pdf_values, where=(x_values < 1), color='skyblue', alpha=0.3, y2=0)
plt.axvline(x=1, color='red', linestyle='--', label='x=1')
plt.text(-1, 0.1, f'P(x < 1 | N(0, 1)) = {probability_x_less_than_1:.2f}', color='black', fontsize=10, ha='left')
plt.title('Part 1: Probability Density Function (PDF) for N(0, 1)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

# Plot the CDF with shaded area
plt.figure(figsize=(10, 5))
plt.plot(x_values, cdf_values, label='CDF')
plt.axvline(x=1, color='red', linestyle='--', label='x=1')
plt.axhline(y=probability_x_less_than_1, color='green', linestyle='--',
            label=f'P(x < 1)={probability_x_less_than_1:.2f}')
plt.scatter(1, probability_x_less_than_1, color='black')  # Intersection point
plt.text(1.5, 0.5, f'P(x < 1 | N(0, 1)) = {probability_x_less_than_1:.2f}', color='black', fontsize=10, ha='left')
plt.title('Part 1: Cumulative Distribution Function (CDF) for N(0, 1)')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()

print(f"Part 1: P(x < 1 | N(0, 1)) = {probability_x_less_than_1:.2f}")

# Part 2
# Given parameters for N(175, 3)
mean_value = 175
std_dev = 3

# Compute the value μ + 2σ
threshold_value = mean_value + 2 * std_dev

# Compute the probability P(x > μ + 2σ)
probability_x_greater_than_threshold = 1 - stats.norm.cdf(threshold_value, loc=mean_value, scale=std_dev)

# Plot the PDF with shaded area for N(175, 3)
x_values_2 = np.linspace(160, 190, 1000)
pdf_values_2 = stats.norm.pdf(x_values_2, loc=mean_value, scale=std_dev)

plt.figure(figsize=(10, 5))
plt.plot(x_values_2, pdf_values_2, label='PDF')
plt.fill_between(x_values_2, pdf_values_2, where=(x_values_2 > threshold_value), color='skyblue', alpha=0.3, y2=0)
plt.axvline(x=threshold_value, color='red', linestyle='--', label=f'x={threshold_value:.2f}')
plt.text(threshold_value + 0.09, 0.02, f'P(x > μ + 2σ | N(175, 3)) = {probability_x_greater_than_threshold:.2f}',
         color='black', fontsize=10, ha='left')
plt.title('Part 2: Probability Density Function (PDF) for N(175, 3)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

# Plot the CDF with shaded area for N(175, 3)
plt.figure(figsize=(10, 5))
cdf_values_2 = stats.norm.cdf(x_values_2, loc=mean_value, scale=std_dev)
plt.plot(x_values_2, cdf_values_2, label='CDF')
plt.axvline(x=threshold_value, color='red', linestyle='--', label=f'x={threshold_value:.2f}')
plt.text(threshold_value + 0.1, 0.8, f'P(x > μ + 2σ | N(175, 3)) = {probability_x_greater_than_threshold:.2f}',
         color='black', fontsize=10, ha='left')
plt.axhline(y=1 - probability_x_greater_than_threshold, color='green', linestyle='--',
            label=f'P(x < 1)={probability_x_greater_than_threshold:.2f}')
plt.scatter([threshold_value], [1-probability_x_greater_than_threshold], color='black')
plt.title('Part 2: Cumulative Distribution Function (CDF) for N(175, 3)')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()

print(f"Part 2: P(x > μ + 2σ | N(175, 3)) = {probability_x_greater_than_threshold:.2f}")
