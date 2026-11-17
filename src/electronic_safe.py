from threading import Thread
from time import sleep
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer

lcd = LCD.lcd()

CORRECT_PIN = [1, 2, 3, 4]
entered = []          # digits typed so far
wrong_count = 0       # number of wrong attempts
state = "locked"      # "locked", "unlocked" or "disabled"


def show_start_screen():
    # REQ-01
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN: ", 2)


def key_pressed(key):
    global entered, wrong_count, state

    # Once unlocked or disabled, ignore all keys
    if state != "locked":
        return

    # * and # are ignored
    if key == "*" or key == "#":
        return

    entered.append(key)

    # REQ-02: show * for each digit, never the digit itself
    lcd.lcd_display_string("Enter PIN: " + "*" * len(entered), 2)

    # Check automatically after the 4th digit
    if len(entered) == 4:
        if entered == CORRECT_PIN:
            # REQ-03
            state = "unlocked"
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Unlocked", 1)
        else:
            wrong_count += 1
            # REQ-04
            lcd.lcd_clear()
            lcd.lcd_display_string("Wrong PIN", 1)
            buzzer.turn_on_with_timer(1)     # buzz for 1 second

            if wrong_count == 3:
                # REQ-05
                state = "disabled"
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Disabled", 1)
            else:
                sleep(2)
                show_start_screen()

        entered = []      # reset for the next try


def main():
    buzzer.init()
    show_start_screen()

    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


if __name__ == "__main__":
    main()