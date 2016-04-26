##afplay
`afplay [song]`

- afplay is a simple music player that comes pre installed with osx
- to play songs at half speed do this: `afplay -r 0.5 -q 1 [song]`

---

#afplay_tools

##afplay_folder.py
`python afplay_folder.py -s/--shuffle [folder]`

- sequentially playas all songs in a folder
- shuffle by passing in `-s` or `--shuffle`
- skip song with `ctl + c`

##afplay_kill.py
`python afplay_kill.py`

- this one will save you from insanity when using the next scripts
- it kills all afplay processes
- by [agner_io](https://gist.github.com/agnerio/9926309)

##afplay_dual.py
`python afplay_dual.py [song]`

- plays song at normal and half speed at the same time
- remember to use `afplay_kill.py` to kill playback

##afplay_spectrum.py
`python afplay_spectrym.py [from speed] [to speed] [steps] [song]`

- plays the song at multiple speeds at once
- waring, if you go over 10 steps you might loose control of volume
- remember to use `afplay_kill.py` to kill playback