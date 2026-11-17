from hal import hal_adc as adc
from hal import hal_servo as servo
from time import sleep


def main():
    # Call each init once (Sections 3 and 4)
    adc.init()
    servo.init()

    while(True):
        # Read the potentiometer (channel 1)
        adc_value = adc.get_adc_value(1)

        # Convert 0-1023 into 180-0 degrees (Figure 3)
        angle = 180 - (adc_value * 180 / 1023)

        print("ADC =", adc_value, " Angle =", round(angle))

        servo.set_servo_position(angle)
        sleep(0.1)  # wait 100ms before reading again


if __name__ == "__main__":
    main()