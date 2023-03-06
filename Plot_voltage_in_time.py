"""
Plot a graphic of the voltage read in time
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ADCPi import ADCPi

YMAX = 0.5


def animate(i, xs, ys, ax, adc, io_channel):
    "Plot the voltage read over time."

    # Read the data
    voltage = adc.read_voltage(io_channel)

    # Insert in current data
    xs.append(i)
    ys.append(voltage)
    xs.pop(0)
    ys.pop(0)

    global YMAX
    YMAX = max(YMAX, voltage)
    mean = np.mean(ys)

    # Plot the data
    ax.clear()
    ax.plot(xs, ys)
    ax.plot([xs[0], xs[-1]], [mean, mean])
    ax.text(xs[0], 1.1*mean, f"{round(mean, 2)}", color="r")

    # Format the plot
    plt.ylim([0, 1.1*YMAX])
    plt.ylabel('Voltage')


if __name__ == "__main__":
    adc = ADCPi(0x68, 0x69, 16)

    io_channel = 2
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = np.zeros(25).tolist()
    ys = np.zeros(25).tolist()
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ax, adc, io_channel), interval=100)


    plt.show()
