import os
import sys
import sndhdr
import random

# check if not 1 or 2 args or if 2 args first arg is shuffle
if (len(sys.argv) not in [2, 3]) or (len(sys.argv) == 3 and sys.argv[1] not in  ['-s', '--shuffle']):
	print('-s/--shuffle [folder]')
else:
	
	# if 2 args shuffle is true
	shuffle = len(sys.argv) == 3
	# first arg if not shuffle else second arg
	folder = sys.argv[1 + int(shuffle)]

	# find songs
	songs = []
	for file in os.listdir(folder):
		if file.split('.')[-1] == 'mp3':
			songs.append(file)
		else:
			path = os.path.join(folder, file)
			try:
				song_data = sndhdr.what(path)
				if song_data:
					songs.append(file)
			except: pass
	print(':: playing', str(len(songs)), 'songs ::')

	# shuffle songs
	if shuffle:
		random.shuffle(songs)
		print(':: shuffle on ::')
	
	# play songs
	for i, song in enumerate(songs):
		print(':: #' + str(i + 1), '::', song, '::')
		song_path = os.path.join(folder, song)
		os.system('afplay "' + song_path + '"')

	print(':: goodnight ::')

	# pause
	#import psutil
	#somepid = 1023
	#p = psutil.Process(somepid)
	#p.suspend()
	#p.resume()	