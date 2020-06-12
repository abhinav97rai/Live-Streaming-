import pafy      #library to pull out api request from youtube
import vlc       #library to push in required api request in VLC media player

ch=0    #variable for channel number
q='a'   #variable to know status of program i.e, to quit or continue

def AAJTAK():
    url = "https://www.youtube.com/watch?v=_QNJA_wFn-o"    #url of live broadcast of aajtak on youtube (**can be changed in future)
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    print("Press q or Q when you want to exit this channel:") #to quit the channel. It can be accessed from python shell or terminal window
    a=input()
    if a=='q'or'Q':
        player.stop()


def ABP():
    url = "https://www.youtube.com/watch?v=AZvGpkxwVIs" #url of live broadcast of abp on youtube (**can be changed in future)
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    print("Press q or Q when you want to exit this channel:") #to quit the channel. It can be accessed from python shell or terminal window
    a=input()
    if a=='q'or'Q':
        player.stop()


def NDTV():
    url = "https://www.youtube.com/watch?v=l9ViEIip9q4" #url of live broadcast of ndtv on youtube (**can be changed in future)
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    print("Press q or Q when you want to exit this channel:") ##to quit the channel. It can be accessed from python shell or terminal window
    a=input()
    if a=='q'or'Q':
        player.stop()

while(q!='yes'):
    #this can be accessed in terminal
    print("Which channel do you want to watch:")
    print("1) AAJTAK")
    print("2) ABP")
    print("3) NDTV")
    print("Enter your channel number(1/2/3): ")
    ch=int(input())
    if ch==1:
        AAJTAK()
    elif ch==2:
        ABP()
    elif ch==3:
        NDTV()
    else:
        print("wrong choice")

    print("Do you want to quit live streaming(enter yes to quit and no to continue): ") #to end the live stream programe 
    q=input()

#if you have any confusion or doubt then please read README-LIVE STREAM file or contact on abhinav96rai@gmail.com