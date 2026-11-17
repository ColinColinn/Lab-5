import time
from hal import hal_lcd as LCD

lcd = LCD.lcd()


def main():
    lcd.lcd_clear()
    show_colon = True

    while(True):
        local_time = time.localtime()   # get current time from the Pi

        # REQ-02: blink only the colons on line 1
        if show_colon:
            time_string = time.strftime("%H:%M:%S", local_time)
        else:
            time_string = time.strftime("%H %M %S", local_time)

        date_string = time.strftime("%d:%m:%Y", local_time)

        # REQ-01: line 1 = time, line 2 = date
        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)

        show_colon = not show_colon     # flip for next second
        time.sleep(1)                   # update every 1 second


if __name__ == "__main__":
    main()