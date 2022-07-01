"""
Plot a graphic of the voltage read in time
"""

import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ADCPi import ADCPi


def animate(i, xs, ys, ax, adc, io_channel, nb_data=25):
    "Plot the voltage read over time."

    # Read the data
    voltage = adc.read_voltage(io_channel)
    xs.append(datetime.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(voltage)

    xs = xs[-nb_data:]
    ys = ys[-nb_data:]
    mean = np.mean(ys)

    # Plot the data
    ax.clear()
    ax.plot(xs, ys)
    ax.plot([xs[0], xs[-1]], [mean, mean])
    ax.text(xs[0], mean, f"mean", color="r")

    # Format the plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over time')
    plt.ylim([0,2])
    plt.ylabel('Voltage')


if __name__ == "__main__":
    adc = ADCPi(0x68, 0x69, 16)
    io_channel = 1

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ax, adc, io_channel), interval=100)
    plt.show()
