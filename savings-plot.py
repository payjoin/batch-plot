import matplotlib.pyplot as plt
import numpy as np

# const cost per input = 67
# const cost per payment = 31
INPUT_COST = 67
OUTPUT_COST = 31
OVERHEAD_COST = 11

def no_batch(n):
    return 140 * n / n

def output_batch(n):
    # 67 vB per input + 31 vB per payment (+ 1 change) + 11vB overhead / per payment
    return (INPUT_COST + OUTPUT_COST * (n+1) + OVERHEAD_COST) / n

def unoptimized_batch(n):
    return (INPUT_COST * n + OUTPUT_COST * (n+1) + OVERHEAD_COST) / n

def payjoin_add_input_batch(n):
    return (INPUT_COST + (OUTPUT_COST * n)) / n

def payjoin_unoptimized_batch(n):
    return (INPUT_COST * n + OUTPUT_COST * n) / n

def payjoin_no_input_batch(n):
    return (OUTPUT_COST * n) / n

# Generate values for n
n_values = np.arange(1, 26)  # From 1 to 25 payments
no_batch_values = no_batch(n_values)

payjoin_no_input_values = payjoin_no_input_batch(n_values)
payjoin_plus_input_values = payjoin_add_input_batch(n_values)
output_batch_values = output_batch(n_values)
payjoin_unoptimized_batch_values = payjoin_unoptimized_batch(n_values)
unoptimized_batch_values = unoptimized_batch(n_values)

# Calculate savings
savings_payjoin_no_input = 100 * (no_batch_values - payjoin_no_input_values) / no_batch_values
savings_payjoin_plus_input = 100 * (no_batch_values - payjoin_plus_input_values) / no_batch_values
savings_output_batch = 100 * (no_batch_values - output_batch_values) / no_batch_values
savings_payjoin_unoptimized_batch = 100 * (no_batch_values - payjoin_unoptimized_batch_values) / no_batch_values
savings_unoptimized_batch = 100 * (no_batch_values - unoptimized_batch_values) / no_batch_values

# Plot the savings
plt.figure(figsize=(10, 4))  # Adjust the figure size to be more narrow

plt.plot(n_values, savings_payjoin_no_input, label='Payjoin no input: 0 inputs, x payments', color='purple')
plt.plot(n_values, savings_payjoin_plus_input, label='Payjoin add input: 1 input, x payments', color='brown')
plt.plot(n_values, savings_output_batch, label='Best case output batch: x inputs, x payments', color='green')
plt.plot(n_values, savings_payjoin_unoptimized_batch, label='Payjoin unoptimized batch: x inputs, x payments', color='orange')
plt.plot(n_values, savings_unoptimized_batch, label='Unoptimized output batch: x inputs, x payments', color='blue')
# Style adjustments
plt.xlabel('Number of payments')
plt.ylabel('Savings')
plt.title('Savings vs Number of payments')
plt.legend(frameon=False)  # Remove the legend box
plt.grid(True, linestyle=':')  # Use fainter dotted grid lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.gca().xaxis.set_ticks_position('bottom')  # Only show ticks on the bottom
plt.gca().yaxis.set_ticks_position('left')  # Only show ticks on the left
plt.gca().tick_params(direction='in')  # Set ticks to point inward

plt.xticks([1, 2, 3, 4, 6, 10, 15, 20, 25])  # Set x-axis ticks to 1, 2, 3, 4
plt.yticks([0, 20, 40, 60, 80], ['0%', '20%', '40%', '60%', '80%'])
plt.xlim(left=1)  # Set the x-axis to start at 1

plt.show()