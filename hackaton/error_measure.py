# Function for calculating the average
def calculate_average(values):
    return sum(values) / len(values)

# List of theoretical and calculated values (to be adapted to your data)
theoretical_values = []
calculated_values = []

# Calculation of averages
theoretical_average = calculate_average(theoretical_values)
calculated_average = calculate_average(calculated_values)

# Calculation of the average error rate
average_error = abs(calculated_average - theoretical_average) / theoretical_average * 100

# Display results
print("Average of theoretical values:", historical_average)
print("Average of calculated values:", calculated_average)
print("Average error rate:", average_error, "%")