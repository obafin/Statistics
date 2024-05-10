import scipy.stats as stats

# Heights of plants in low light and high light conditions
low_light = [49, 31, 43, 31, 40, 44, 49, 48, 33]
high_light = [45, 40, 59, 58, 55, 50, 46, 53, 43]

# Perform the T-test for the means of two independent samples
t_statistic, p_value = stats.ttest_ind(low_light, high_light)

print("T-statistic:", t_statistic)
print("P-value:", p_value)
