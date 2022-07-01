from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    flexi = [16.7, 17.4, 18.4, 19.3, 24, 27.5, 28, 32, 38]
    distrilec = [503, 630, 814, 961, 1110, 1270, 1430, 1540, 1650]
    old = [160, 270, 330, 370, 410, 485, 525, 595, 705]
    x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 35+11.4])
    x += 24

    plt.figure()
    plt.plot(x, flexi, '.', label="flexi")
    plt.xlabel("volume")
    plt.ylabel("voltage [mV]")
    plt.legend()

    plt.figure()
    plt.plot(x, distrilec, '.', label="distrilec")
    plt.xlabel("volume")
    plt.ylabel("voltage [mV]")
    plt.legend()

    plt.figure()
    plt.plot(x, old, '.', label="old")
    plt.xlabel("volume")
    plt.ylabel("voltage [mV]")
    plt.legend()
    plt.show()
