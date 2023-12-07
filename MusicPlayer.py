#IMPORT IMPORTANAT LIBRARIES

import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("SD Music Player")
root.geometry("485x700+290+10")
root.configure(background='Gray')
root.resizable(False, False)
mixer.init()

# CREATE A FUNCTION TO OPEN A FILE

def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    
    
# icon
lower_frame = Frame(root , bg = "white", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)


# SET LOGO OF THE MUSIC PLAYER

image_icon = PhotoImage(file="SD logo.png")
root.iconphoto(False, image_icon)


frameCnt = 30
frames = [PhotoImage(file='noti.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=-85, y=0)
root.after(0, update, 0)




# CODE FOR BUTTONS OF MUSIC PLAYER

PlayButton = PhotoImage(file="play1.png")
Button(root, image=PlayButton, bg="white", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=215, y=487)

StopButton = PhotoImage(file="stop11.png")
Button(root, image=StopButton, bg="white", bd=0, height = 60, width =60,
       command=mixer.music.stop).place(x=130, y=487)

volumeButton = PhotoImage(file="volume.png")
Button(root, image=volumeButton, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=20, y=487)

PauseButton = PhotoImage(file="pause1.png")
Button(root, image=PauseButton, bg="white", bd=0, height = 60, width =60,
       command=mixer.music.pause).place(x=300, y=487)

# Label       
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)


# CODE FOR BROWSE THE MUSIC FROM FOLDER

Button(root, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="white", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="gray", fg="black", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# EXECUTE Tkinter

root.mainloop()