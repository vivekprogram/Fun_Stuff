from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter as tk
import eyed3
from pygame import mixer

root = tkinter.Tk()
fr = Frame(root)
fr.pack()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack()

menubar = Menu(root)
root.config(menu=menubar)

subMenu  = Menu(menubar,tearoff=0)
def browse_file():
	global filename
	filename = filedialog.askopenfilename(initialdir="./songs",title="Select Song",filetypes =[('MPEG Audio Layer 3', '*.mp3')])
	mixer.music.load(filename)
	song = eyed3.load(filename)
	q = song.tag.album
	w = song.tag.title
	text1 = Label(fr,text=q)
	text1.pack(side=tk.TOP)
	text = Label(fr,text=w)
	text.pack(side=tk.TOP)


menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open",command=browse_file)
subMenu.add_command(label="Exit",command=root.destroy)

def about_us():
	tk.messagebox.showinfo('About Melody','This is a music player build using python Tkinter by @saripella')

subMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About Us",command=about_us)

mixer.init()
paused = False
root.geometry('300x300')
root.title('Music')


def play_music():
	mixer.music.play()
	statusbar['text'] = "Playing Music.."

def stop_music():
	mixer.music.stop()
	statusbar['text'] = "Music Stopped"

def pause_music():
	global paused
	if paused == False:
		paused=True
		mixer.music.pause()
		statusbar['text'] = "Music Paused"
	elif paused == True:
		paused=False
		mixer.music.unpause()
		statusbar['text'] = "Music playing.."

def set_vol(val):
	volume = int(val)/100
	mixer.music.set_volume(volume)

playPhoto = PhotoImage(file='start1.png')
playBtn = Button(frame,image=playPhoto,width=45,height=45,command=play_music)
playBtn.pack(side=LEFT)

stopPhoto = PhotoImage(file='stop1.png')
stopBtn = Button(frame,image=stopPhoto,width=45,height=45,command=stop_music)
stopBtn.pack(side=LEFT)

pausePhoto = PhotoImage(file='pause1.png')
pauseBtn = Button(frame,image=pausePhoto,width=45,height=45,command=pause_music)
pauseBtn.pack(side=LEFT)

scale = Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,length=150,label='Volume Bar : ',showvalue=0,command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(side=BOTTOM)

loader = Button(root,text="Load Song",fg="blue",command=browse_file)
loader.pack()

statusbar = Label(root,text="Welcome to Music Player made by @saripella",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
