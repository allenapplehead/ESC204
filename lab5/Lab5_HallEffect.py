'''
ESC204S 2023 Lab 5, Task B
Task: Take readings using a Hall effect sensor.
'''

import time
import board
import analogio
# set display to show either ADC output representative integer or
# the voltage that it represents
INT_MODE = 0
VOLT_MODE = 1
mode = INT_MODE
# always 0xff (in hex) according to: https://learn.adafruit.com/
# circuitpython-basics-analog-inputs-and-outputs/
# analog-to-digital-converter-inputs
ADC_HIGH = 65535
# set up sensor as analog input over analog pin A0
# (on GPIO pin 26 for Pico, needs to be changed if using Nano)
sensor_pin = board.A0
sensor = analogio.AnalogIn(sensor_pin)
# show reference voltage (logic high, 3.3V) and the
# corresponding analog integer value
ADC_REF = sensor.reference_voltage
print("ADC reference voltage: {}".format(ADC_REF))
print("ADC high voltage integer value: {}".format(ADC_HIGH))
# convert ADC input value back to voltage
def adc_to_voltage(adc_value):
    return  ADC_REF * (float(adc_value)/float(ADC_HIGH))
# take readings from sensor
while True:
    # read adc value and print
    if mode == INT_MODE:
        print((sensor.value,))
    # convert to voltage
    else:
        print((adc_to_voltage(sensor.value),))
    time.sleep(0.5)
