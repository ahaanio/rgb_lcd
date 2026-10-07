from machine import Pin, I2C
import time
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq = 400000)
devices = i2c.scan()
i2c_address = devices[0]
lcd = I2cLcd(i2c, i2c_address, 2, 16)

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
blue = Pin(13, Pin.OUT)

button1 = Pin(16, Pin.IN, Pin.PULL_UP)
button2 = Pin(21, Pin.IN, Pin.PULL_UP)
button3 = Pin(18, Pin.IN, Pin.PULL_UP)

red_is_on = False
green_is_on = False
blue_is_on = False

while True:
    button_pressed = False
    
    if button1.value() == 0:
        red_is_on = not red_is_on
        red.value(red_is_on)
        button_pressed = True
        
    if button2.value() == 0:
        green_is_on = not green_is_on
        green.value(green_is_on)
        button_pressed = True
        
    if button3.value() == 0:
        blue_is_on = not blue_is_on
        blue.value(blue_is_on)
        button_pressed = True


    if button_pressed:
        lcd.clear()
        lcd.move_to(0,0)
        
        if red_is_on and green_is_on and blue_is_on:
            lcd.putstr("White")
        
        elif red_is_on and green_is_on:
            lcd.putstr("Yellow")
        elif green_is_on and blue_is_on:
            lcd.putstr("Cyan")
        elif blue_is_on and red_is_on:
            lcd.putstr("Purple")
        
        elif red_is_on:
            lcd.putstr("Red")
        elif green_is_on:
            lcd.putstr("Green")
        elif blue_is_on:
            lcd.putstr("Blue")
        else:
            lcd.putstr("All Off")
            
        time.sleep(0.3) 

    time.sleep(0.05)
