#In this assignment, you will build a Savings Progress Chart using Matplotlib. 
# You will plot weekly savings as a line graph, add labels and a title, customise the line, and compare the same data using a bar chart.

import matplotlib.pyplot as plt

week = [1, 2, 3, 4, 5, 6]
savings = [300, 200, 150, 400, 700, 800]

plt.plot(week, savings, color='blue', marker='o', linestyle='dashed',linewidth=2)
plt.title('Savings Progress Chart')
plt.plot(week, savings)
plt.xlabel('Week No.')
plt.ylabel('savings')
plt.grid(True)
plt.ylim(0,1000)
plt.show()

plt.bar(week, savings, color='orange')
plt.title('Savings Progress Chart')
plt.xlabel('Week No.')
plt.ylabel('Savings')
plt.ylim(0,1000)
plt.show()