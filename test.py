import numpy as np
import time
import matplotlib.pyplot as plt
from ADCPi import ADCPi
from IOPi import IOPi

if __name__ == "__main__":
    adc = ADCPi(0x68, 0x69, 16)
    iobus = IOPi(0x20)
    adc.set_pga(1)
    adc.set_bit_rate(18)

    light_pin = 1
    iobus.set_pin_direction(1,0)
    weight_pin = 8
    OD_pin = 7

    while True:
        iobus.write_pin(light_pin, 1) # Lights on
        time.sleep(1)
        # weight_voltage = adc.read_voltage(weight_pin) # Measure weight
        OD_value = adc.read_voltage(OD_pin) # Measure OD
        time.sleep(1)
        iobus.write_pin(light_pin, 0) # lights off
        # print(f"Weight voltage: {weight_voltage}")
        print(f"OD voltage: {OD_value}")
        time.sleep(2)
