import os
import matplotlib.pyplot as plt

current_working_directory = os.getcwd()

# Data to plot
funding_goal = 11500
labels = ['Payment to Artists', 'Kickstarter fee', 'Payment \nprocessing fees', 'Printing and Shipping']
sizes = [5960, funding_goal*0.05, 410.2, 4442]
colors = ['forestgreen', 'gold', 'yellow', 'yellowgreen']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
figure_path = os.path.join(current_working_directory, "ProjectBudget.png")
plt.figure(dpi=200)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=0)

plt.axis('equal')
plt.tight_layout()
plt.savefig(figure_path)
plt.show()