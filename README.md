# SIT210-Task5.2CGUI
 S306 SIT210 Task 5.2C, control some LEDs with a GUI, with added brightnesss control for that 21st century feeling!

## Description
A simple GUI with radio buttons and a slider to control a set of LEDs on a Raspberry Pi 5.

When a radio button is selected, that LED is turn on, and the rest off. If the LED is a PWM LED, then the value is set to that of the slider through the `set_pwm` helper function.
There is also an exit button so the GUI can safely close.

## How it Works
Most functions work as per [Task 5.1P](https://github.com/s223484777/SIT210-Task5.1PGUI), with the exception of the slider and PWNLED setup.

Set up a `PWMLED`:
```python
pwm_led = gpiozero.PWMLED(19, active_high=False)] # Create a PWM LED on pin 19 that is active low
```

Set the PWM value in a PWMLED:
```python
pwm_led.value = 0.25 # Set the value of the PWM LED from 0.0 to 1.0
``` 

Setting up the slider and defaulting the value to 50 (half brightness): 
```python
# Create the slider
slider = tk.Scale(window, from_=0, to=100, orient="horizontal", command=set_pwm)

# Set the slider's value to 50
slider.set(50)
```

Raspberry Pi 5 PWM pins are:
GPIO 12
GPIO 13
GPIO 18
GPIO 19

Ensure the PWM LEDs are attached to these pins.

## Usage
Requires the following libraries:
* gpiozero
* tkinter