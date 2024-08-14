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

def payjoin_add_input_batch(n):
    return (INPUT_COST + (OUTPUT_COST * n)) / n

def payjoin_no_input_batch(n):
    return (OUTPUT_COST * n) / n


# Generate values for n
n_values = np.arange(1, 26)  # From 1 to 25 payments
no_batch_values = no_batch(n_values)
output_batch_values = output_batch(n_values)
payjoin_plus_input_values = payjoin_add_input_batch(n_values)
payjoin_no_input_values = payjoin_no_input_batch(n_values)

# Plot the functions
plt.figure(figsize=(10, 4))  # Adjust the figure size to be more narrow
plt.plot(n_values, no_batch_values, label='No batch', color='green')
plt.plot(n_values, output_batch_values, label='Output-only batching', color='red')
plt.plot(n_values, payjoin_plus_input_values, label='Payjoin cut-through plus receiver input', color='blue')
plt.plot(n_values, payjoin_no_input_values, label='Payjoin cut-through with no additional inputs', color='purple')

# Style adjustments
plt.xlabel('Number of payments')
plt.ylabel('Vbytes per payment')
plt.title('Vbytes per payment vs Number of payments')
plt.legend(frameon=False)  # Remove the legend box
plt.grid(True, linestyle=':')  # Use fainter dotted grid lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.gca().xaxis.set_ticks_position('bottom')  # Show ticks on the bottom
plt.gca().yaxis.set_ticks_position('left')  # Show ticks on the left
plt.gca().tick_params(direction='in')  # Set ticks to point inward

plt.xticks([1, 2, 3, 4, 6, 10, 15, 20, 25])  # Set x-axis ticks to 1, 2, 3, 4
plt.yticks([0, 50, 100, 150])
plt.xlim(left=1)  # Set the x-axis to start at 1

plt.show()