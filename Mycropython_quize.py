#This script is like a quiz thing, if one button is pressed it will light up an LED by it and will disable the other LED by the other Button until a quizmaster switch is pressed.
#LEDs connected to GPIO pins 14 and 15, buttons connected to GPIO pins 12, 13, and 16, pull down resistors are not needed.
#Be sure to use 150Ω resistors between the LEDs and ground

from machine import Pin #Loads machine library, which allows us to control GPIO pins
import utime            #Loads microtime library, which allows us to control GPIO pins

#Set the GPIO pins used for the LEDs as a variable.
yellow_led_pin = 14 #yellow
blue_led_pin = 15 #red

#set the GPIO pins used for the buttons as a variable.
yellow_btn_pin = 12 #yellow
blue_btn_pin = 13 #red
reset_btn_pin = 16 #reset

#Set the LEDs/Buttons as an output/input.
yellow_led = Pin(yellow_led_pin, Pin.OUT)              
blue_led = Pin(blue_led_pin, Pin.OUT)
yellow_btn = Pin(yellow_btn_pin, Pin.IN, Pin.PULL_DOWN)
blue_btn = Pin(blue_btn_pin, Pin.IN, Pin.PULL_DOWN)
reset_btn = Pin(reset_btn_pin, Pin.IN, Pin.PULL_DOWN)

# turn everything off before starting
yellow_led.off()
blue_led.off()

while True:
    utime.sleep(0.001)
    if yellow_btn.value() == 1:
        yellow_led.on()
        while reset_btn.value() != 1: # must press reset before other light can be activated
            utime.sleep(0.001)
        else:
            yellow_led.off()
    elif blue_btn.value() == 1:
        blue_led.on()
        while reset_btn.value() != 1: # must press reset before other light can be activated
            utime.sleep(0.001)
        else:
            blue_led.off()               