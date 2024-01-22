import matplotlib.pyplot as plt
import numpy as np
# Data for plotting, updated with the provided values
categories = ['L-1', 'L-2', 'L-3']
discounted_returns_1 = [7.83, 8.83, 9.91]  # Updated data
discounted_returns_2 = [6.43, 7.24, 6.89]
discounted_returns_3 = [2.02, 2.46, 2.46]
discounted_returns_4 = [0.10, 0.10, 0.36]
discounted_returns_5 = [16.71, 17.06, 20.33]
discounted_returns_6 = [8.19, 9.65, 15.90]
discounted_returns_7 = [15.71, 17.18, 16.43]
discounted_returns_8 = [0.00, 2.18, 3.65]

# Data for plotting, updated with the provided values
fig, axs = plt.subplots(2, 4, figsize=(20, 10))
all_returns = [discounted_returns_1, discounted_returns_2, discounted_returns_3, discounted_returns_4,
               discounted_returns_5, discounted_returns_6, discounted_returns_7, discounted_returns_8]

ax = axs[0, 0]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[0]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(7, 10.5)
ax.set_yticks([7,8,9,10])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchPick', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[0, 1]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[1]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(6, 7.75)
ax.set_yticks([6.0,6.5,7.0,7.5])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchPush', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[0, 2]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[2]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(1.5, 2.75)
ax.set_yticks([1.5,2.0,2.5])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchReach', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[0, 3]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[3]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(0.0, 0.5)
ax.set_yticks([0.0,0.2,0.4])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchSlide', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[1, 0]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[4]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(15, 22)
ax.set_yticks([16,18,20,22])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchPick', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[1, 1]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[5]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(7.5, 17.5)
ax.set_yticks([10, 15])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchPush', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[1, 2]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[6]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(14, 18)
ax.set_yticks([14,15,16,17,18])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchReach', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

ax = axs[1, 3]
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)
discounted_returns = all_returns[7]
bars = ax.bar(categories, discounted_returns, color='none', edgecolor=['orange', 'green', 'blue'], hatch='/')
ax.set_ylim(0, 5)
ax.set_yticks([0,2,4])
ax.tick_params(axis='both', which='major', labelsize=38)  # Larger y-axis tick labels
ax.set_title('FetchSlide', fontsize=38)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), verticalalignment='bottom', ha='center', fontsize=35)

# Adjust layout for better visibility
plt.tight_layout()

# Show the plot
plt.savefig('rero_gcrl.png')