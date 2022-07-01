"""
Plot a graphic of the voltage read in time
"""

from __future__ import absolute_import, division, print_function, \
    unicode_literals
import time
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ADCPi import ADCPi


def animate(i, xs, ys, adc, io_channel, nb_data=50):
    "Plot the voltage read over time."

    # Read the data
    voltage = adc.read_voltage(io_channel)
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(voltage)

    xs = xs[-nb_data:]
    ys = ys[-nb_data:]

    # Plot the data
    ax.clear()
    ax.plot(xs, ys)
    ax.plot([xs[0], xs[-1]], [np.mean(ys), np.mean(ys)], "r-")

    # Format the plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over time')
    plt.ylabel('Voltage')


if __name__ == "__main__":
    adc = ADCPi(0x68, 0x69, 12)
    io_channel = 8

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, adc, io_channel), interval=200)
    plt.show()
