import sys
import subprocess

if len(sys.argv) != 5:
	print('[from speed] [to speed] [steps] [song]')
else:

	range_from = float(sys.argv[1])
	range_to = float(sys.argv[2])
	count = int(sys.argv[3])
	song = sys.argv[4]

	if count < 2:
		print('[steps] needs to be 2 or more')
	else:
		proceed = True
		if count > 10:
			sys.stdout.write('warnign! you might loose volume control. proceed on own risk. run afplay_kill.py if you cant handel it. type "hit me" to proceed:')
			response = input()
			if response != 'hit me':
				proceed = False
		if proceed:
		
			width = abs(range_to - range_from)
			spectrum = [min(range_from, range_to) + (width / (count - 1)) * i for i in range(count)]

			print('speed spectrum:', spectrum)

			for speed in spectrum:
				subprocess.Popen(['afplay', '-r', str(speed), '-q', '1', song])