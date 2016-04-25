import os
import sys
import sndhdr

if len(sys.argv) != 2:
	print('[folder]')
else:

	folder = os.path.abspath(sys.argv[1])
	
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

	print('found', str(len(songs)), 'songs')

	for i, song in enumerate(songs):
		print('playing #' + str(i + 1), song)
		song_path = os.path.join(folder, song)
		os.system('afplay "' + song_path + '"')