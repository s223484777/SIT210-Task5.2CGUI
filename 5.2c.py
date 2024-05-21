#!/usr/bin/env python

import gpiozero
import tkinter as tk

# Setup LEDs
leds = [gpiozero.LED(2),                     # GPIO  2, Blue LED anode
	gpiozero.LED(3),                     # GPIO  3, Dual LED green anode
	gpiozero.LED(4),                     # GPIO  4, Dual LED red anode
	gpiozero.PWMLED(12, active_high=False), # GPIO 12, RGB LED blue cathode
	gpiozero.PWMLED(13, active_high=False), # GPIO 13, RGB LED green cathode
	gpiozero.PWMLED(19, active_high=False)] # GPIO 19, RGB LED red cathode
for led in leds: led.off()
pwm_val = 0.0

# Setup Tkinter window
window = tk.Tk()
window.title("LED Controller")

# Update the LED states to match the current selection
selected = tk.IntVar()
def update():
  for i in range(0, len(leds)):
    if i == selected.get():
      if i in (3,4,5):
        leds[i].value = pwm_val
      else:
        leds[i].on()
    else:
      leds[i].off()

# Set the PWM value and update the LEDs
def set_pwm(val):
  global pwm_val
  pwm_val = int(val) / 100.0
  update()

# Setup labels
labels = [tk.Label(window, text="Single LED Blue", width=24),
	  tk.Label(window, text="Dual LED Green", width=24),
	  tk.Label(window, text="Dual LED Red", width=24),
	  tk.Label(window, text="RGB LED Blue", width=24),
	  tk.Label(window, text="RGB LED Green", width=24),
	  tk.Label(window, text="RGB LED Red", width=24),
          tk.Label(window, text="Brightness", width=24)]
for i in range(len(labels)): labels[i].grid(row=i, column=0)

# Set up the buttons
buttons = [tk.Radiobutton(window, variable=selected, value=i, command=update) for i in range(0, 6)]
for i in range(len(buttons)):
  buttons[i].grid(row=i, column=1)

# Set up the brightness slider
slider = tk.Scale(window, from_=0, to=100, orient="horizontal", command=set_pwm)
slider.set(50)
slider.grid(row=len(buttons), column=1)

# Set up the exit button
buttons.append(tk.Button(window, text="Exit", command=window.destroy))
buttons[-1].grid(row=len(buttons)+1, column=1)

# Update the initial status and run the main loop
update()
window.mainloop()
