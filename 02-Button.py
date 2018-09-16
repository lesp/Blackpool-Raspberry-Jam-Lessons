from gpiozero import Button

button = Button(2)

button.wait_for_press()
print("Button was pressed")

#Can you add another button?
#Can you turn on an LED each time the button is pressed?