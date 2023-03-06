from matplotlib import pyplot as plt
import numpy as np

def sensor_comparison():
    "Comparing brands of sensors"
    flexi = [16.7, 17.4, 18.4, 19.3, 24, 27.5, 28, 32, 38]
    distrilec = [503, 630, 814, 961, 1110, 1270, 1430, 1540, 1650]
    old = [160, 270, 330, 370, 410, 485, 525, 595, 705]
    x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 35+11.4])
    x += 24

    plt.figure()
    plt.plot(x[:-1], flexi[:-1], '.', label="flexi", color="C0")
    fit = np.polyfit(x[:-1], flexi[:-1], 1)
    plt.plot(x[:-1], np.polyval(fit, x[:-1]), '-', color="C0")

    plt.plot(x, distrilec, '.', label="distrilec", color="C1")
    fit = np.polyfit(x, distrilec, 1)
    plt.plot(x, np.polyval(fit, x), '-', color="C1")

    plt.plot(x, old, '.', label="old", color="C2")
    fit = np.polyfit(x, old, 1)
    plt.plot(x, np.polyval(fit, x), '-', color="C2")

    plt.xlabel("grams")
    plt.ylabel("voltage [mV]")
    plt.legend()

def distrilec_comparison():
    "Comparing 3 identical sensors from the distrilec brand"
    v1 = [500, 630, 750, 880, 1010, 1140, 1240, 1380, 1740]
    v2 = [730, 860, 980, 1060, 1200, 1320, 1410, 1500, 1660]
    v3 = [500, 600, 710, 820, 930, 1030, 1130, 1240, 1440]
    x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 35+11.4])
    x += 24

    plt.plot(x, v1, '.', label="sensor 1", color="C0")
    fit = np.polyfit(x, v1, 1)
    plt.plot(x, np.polyval(fit, x), '-', color="C0")

    plt.plot(x, v2, '.', label="sensor 2", color="C1")
    fit = np.polyfit(x, v2, 1)
    plt.plot(x, np.polyval(fit, x), '-', color="C1")

    plt.plot(x, v3, '.', label="sensor 3", color="C2")
    fit = np.polyfit(x, v3, 1)
    plt.plot(x, np.polyval(fit, x), '-', color="C2")
    
    plt.xlabel("grams")
    plt.ylabel("voltage [mV]")
    plt.legend()


def distrilec_padsize():
    "Comparing pad sizes on the 3 sensors"
    s1_small = [[650, 1340], [690, 1380]]
    s2_small = [[1280, 1870], [1380, 1900]]
    s3_small = [[930, 1720], [1050, 1800]]
    s1_big = [[330, 1160], [600, 1250]]
    s2_big = [[800, 1330], [900, 1520]]
    s3_big = [[910, 1800], [980, 1960]]
    x = np.array([0, 35+11.4])
    x += 24

    plt.fill_between(x, s1_small[0], s1_small[1], alpha=0.5, label="s1_small")
    plt.fill_between(x, s2_small[0], s2_small[1], alpha=0.5, label="s2_small")
    plt.fill_between(x, s3_small[0], s3_small[1], alpha=0.5, label="s3_small")
    plt.fill_between(x, s1_big[0], s1_big[1], alpha=0.5, label="s1_big")
    plt.fill_between(x, s2_big[0], s2_big[1], alpha=0.5, label="s2_big")
    plt.fill_between(x, s3_big[0], s3_big[1], alpha=0.5, label="s3_big")
    
    plt.xlabel("grams")
    plt.ylabel("voltage [mV]")
    plt.legend()



if __name__ == "__main__":
    sensor_comparison()
    # distrilec_comparison()
    # distrilec_padsize()

    plt.show()
