import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

color = 'cornflowerblue'

points = np.ones(5)
text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'monospace'})


def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()


def nice_repr(text):
    return repr(text).lstrip('u')

fig, (ax, ax1) = plt.subplots(2, 1)

linestyles = ['-', '--', '-.', ':']

# line styles draw
for y, linestyle in enumerate(linestyles):
    ax.text(-0.1, y, nice_repr(linestyle), **text_style)
    ax.plot(y * points, linestyle=linestyle, color=color, linewidth=3)
    format_axes(ax)
    ax.set_title('line styles')

# line marker draw
marker_style = dict(color=color, linestyle=':', marker='o',
                    markersize=15, markerfacecoloralt='gray')
for y1, fill_style in enumerate(Line2D.fillStyles):
    ax1.text(-0.3, y1, nice_repr(fill_style), **text_style)
    ax1.plot(y1 * points, fillstyle=fill_style, **marker_style)
    format_axes(ax1)
    ax1.set_title('fill styles')


plt.show()
