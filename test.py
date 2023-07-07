import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ADCPi import ADCPi
from IOPi import IOPi

if __name__ == "__main__":
    adc = ADCPi(0x68, 0x69, 14)
    adc.set_pga(1)
    adc.set_bit_rate(14)

    WS_current_pin = 1
    WS_flexi_pin = 2

    dt = 1
    times = np.arange(0, 30, dt)
    voltages = pd.DataFrame(columns=["WS current", "WS flexi"])

    print("Starting reading...")
    for ii in range(len(times)):
        voltages.loc[ii] = [
            np.mean([adc.read_voltage(WS_current_pin) for jj in range(10)]),
            np.mean([adc.read_voltage(WS_flexi_pin) for jj in range(10)]),
        ]

        time.sleep(dt)
    print("Finished reading.")

    plt.figure()
    plt.legend(labels=["WS current", "WS flexi"])
    plt.plot(times, voltages)
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [V]")
    plt.grid()
    plt.show()
