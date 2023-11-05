import serial
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
while True:
	data = arduino.readline()
	if data:
		print data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason
