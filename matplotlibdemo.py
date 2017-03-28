
import matplotlib.pyplot as plt
import numpy as np


fig, (ax, ax1, ax2, ax3) = plt.subplots(4, 1)
# example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))

performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))


ax.barh(
    y_pos, performance, xerr=error, align='center', color='red', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')


x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)


ax1.fill(x, y, zorder=10)
ax1.grid(True, zorder=5)


x1 = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x1)
y2 = np.sin(3 * x1)

ax2.fill(x1, y1, 'b', x1, y2, 'r', alpha=0.3)


x2 = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]

line1, = ax3.plot(
    x2, np.sin(x2), '--', linewidth=2, label='Dashes set retroactively')
line1.set_dashes(dashes)

line2, = ax3.plot(
    x2, -1 * np.sin(x2), dashes=[30, 5, 10, 5], label='Dashes set proactively')
ax3.legend(loc='lower right')


plt.show()
