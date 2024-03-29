import numpy as np
from pynput import keyboard
import time
import datetime
from ADCPi import ADCPi

# test

def measure_start(key, adc, io_channel):
    if key == keyboard.Key.enter: # Measuring voltage
        print("")
        print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')}: Starting measure")
        time.sleep(5)
        v = []
        t = 0
        while t < 5:
            v.append(adc.read_voltage(io_channel))
            t += 0.1
        print(f"Finished measure, mean voltage: {round(np.mean(v),2)}")

    elif key == keyboard.Key.esc: # Stopping program
        return False


if __name__ == "__main__":
    adc = ADCPi(0x68, 0x69, 16)
    io_channel = 1

    with keyboard.Listener(on_press = lambda event: measure_start(event, adc, io_channel)) as listener:
        listener.join()
