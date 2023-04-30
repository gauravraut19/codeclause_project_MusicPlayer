import os
import fnmatch
import tkinter as tk
from pygame import mixer

canvas = tk.Tk()
canvas.geometry("500x400")
canvas.wm_title("Spotify Mp3")
canvas.config(bg='silver')

rootpath = "C:\\Users\Hp\OneDrive\Desktop\music"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"



listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=(18))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg="yellow", font=(18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text="Prev", command= play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", command= stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", command= pause_song)
stopButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", command= play_next)
nextButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
