import explorerhat as eh
import time, random

for x in range(10):
	led = random.choice([0,1,2,3])
	for y in range(2):
	#eh.output[led].on()
		eh.output[led].toggle()
		time.sleep(1)
	#eh.output[led].off()
