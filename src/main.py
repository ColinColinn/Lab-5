from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control

lcd = LCD.lcd()
lcd.lcd_clear()


# Called by the keypad driver whenever a key is pressed
def key_pressed(key):
    print(key)

    if key == 1:                          # REQ-02: blink
        led_control.delay = 1
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blink LED", 2)

    elif key == 0:                        # REQ-03: off
        led_control.delay = 0
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("OFF LED", 2)

    # REQ-04: any other key -> do nothing


def main():
    # REQ-01: start-up screen
    lcd.lcd_clear()
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1:Blink", 2)

    # Start the keypad
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    # Start the LED thread (LED is off because delay = 0)
    led_control.led_control_init()


if __name__ == "__main__":
    main()