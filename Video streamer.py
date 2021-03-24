import pafy
from tkinter import *
import vlc
import time
from stopwatch import Stopwatch
root = Tk()
root.geometry('800x500')
link = ''
bg = PhotoImage(file="background.PNG")
#making canvas

#making input box for entering URL
photo_label= Label(root,image=bg)
photo_label.place(x=0,y=0,width=800,height=500)
entry_frame = Frame(root,bg="#cfcfe2")
entry_frame.pack(pady=180)
button_frame = Frame(root)
button_frame.pack(pady=0)
url_enter = Entry(entry_frame,width = 50,bg = "#8c56b3")
url_enter.pack()
#------------------------------------------------------------------
#function to make button do something in this case:-
#take URL and print its title along with playing the video

def submit_url():
    link = url_enter.get()
    video = pafy.new(link)
    global best
    best = video.getbest()
    playurl = best.url
    Instance = vlc.Instance()
    global player
    player = Instance.media_player_new()
    media = Instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()
    mylabel = Label(root,text = video.title)
    mylabel.pack()
    duration = video.length
    

def pause():
    player.pause()
def end():
    player.stop()
def resume():
    player.play()
def download():
    best.download()
#function end
#making button for inputting the URL
button = Button(entry_frame, text = "Submit URL",command = submit_url)
button.pack()
pause_btn = Button(entry_frame,text = "pause",command = pause)
pause_btn.pack()
stop_btn = Button(entry_frame,text="stop",command = end)
stop_btn.pack()
resume_btn=Button(entry_frame,text="resume",command = resume)
resume_btn.pack()
download_btn = Button(entry_frame,text = 'download',command = download)
download_btn.pack()
#__button made___
#------------------------------------------------------------------
root.mainloop()
