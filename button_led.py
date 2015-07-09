import explorerhat as eh

def wait_for_press(button,event):
	if button <= 4:
		led = button - 1
		if event == 'press':
			eh.light[led].on()
		else:
			eh.light[led].off()
while True:
	eh.touch.pressed(wait_for_press)
	eh.touch.released(wait_for_press)
