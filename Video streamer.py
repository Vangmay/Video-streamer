#this program will take a youtube url from user and will fetch the video and the title from it,then display the video to the user.
import pafy
from tkinter import *
import vlc
root = Tk()
link = ''
#making input box for entering URL
url_enter = Entry(root,width = 50)
url_enter.pack()
#------------------------------------------------------------------
#function to make button do something in this case:-
#take URL and print its title along with playing the video
def submit_url():
    link = url_enter.get()
    video = pafy.new(link)
    best = video.getbest()
    playurl = best.url
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    media = Instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)
    player.play()
    mylabel = Label(root,text = video.title)
    mylabel.pack()
#function end
#making button for inputting the URL
button = Button(root, text = "Submit URL",command = submit_url)
button.pack()
#__button made___
#------------------------------------------------------------------
root.mainloop()
