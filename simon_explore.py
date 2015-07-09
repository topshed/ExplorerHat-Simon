import explorerhat as eh
import time, random

target_seq = [] # List to store the sequence that will be displayed
global user_seq # Global because we'll change it via a function
user_seq = [] # List to hold the sequence entered by player
leds_list= [1,2,3,4] # The output LEDs

def wait_for_press(c,e): # Handler to run when button pressed
	if c > 4: # Crocodile pads don't have LEDs...
		led = c - 5 # ...so map to button LEDs
	else:
		led = c - 1 # Button LEDs are 0-3, outputs 1-4
	if e == 'press': # Turn on the appropriate button LED
		eh.light[led].on()
	else:
		eh.light[led].off()
		user_seq.append(led + 1) # Add to player sequence

# Main program
print('Starting. Replay the sequence before time runs out.')
level = 0
GameOn = True # If True then a game is active
gap = 0.8 # Sets the speed of flashing
while GameOn:
	user_seq = [] #Clear sequence
	level+=1
	count = 1 # Number of steps in sequence
	print('Starting Level ' + str(level))
	for i in  range(count): # create a target sequence
		led = random.choice(leds_list) # Pick random LED
		target_seq.append(led) # Add to sequence
	for seq_n in target_seq: # Display the sequence
		for t in range(2):
			eh.output[seq_n-1].toggle()
			time.sleep(gap)
	eh.touch.pressed(wait_for_press) # Wait for player to press buttons
	eh.touch.released(wait_for_press)
	countdown = 20 # Amount of time player has for each level
	waiting = True
	while waiting:
		if (len(user_seq) == len(target_seq)) or (countdown == 0):
			if user_seq == target_seq: # Did the player get it right?
				waiting = False
				time.sleep(0.5)
				print('Correct')
				eh.light.on() # flash all LEDs to celebrate success
				eh.output.on()
				time.sleep(0.4)
				eh.light.off()
				eh.output.off()
				gap = gap* 0.8 # make the next round faster
			else:
				waiting = False
				GameOn = False # Game Over
				print('Game Over: You reached level: ' + str(level))
				eh.pause() # Cleanup
		time.sleep(1) # Brief pause between levels
		countdown-=1 # Decrement countdown
		print countdown # display countdown to console

