import sys
import subprocess
if len(sys.argv) != 2:
	print('[song]')
else:
	song = sys.argv[1]
	subprocess.Popen(['afplay', song])
	subprocess.Popen(['afplay', '-r', '0.5', '-q', '1', song])