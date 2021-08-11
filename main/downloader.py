import requests
import os #you will need incase you want to store the vid in a specific folder/path
from pytube import *

print('''
█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀           A PIKACHU FOR YOU 
''')



print("""Do you want to download video from youtube or Some other website ?
         For YouTube Choose 1 and Choose 2 for some other website.""")


a = int(input("Enter Your Choice [1 or 2] : "))

if a == 1 :
    url = input("Please enter the YouTube video URL : ")
    youtube = YouTube(url)
    video = youtube.streams.first()
    video.download()
    print("Video Downloaded!")
    print(video.title)

  

elif a == 2:
    c = input("Please provide the url of the Video/Audio File : ")
    r= requests.get(c,stream=True)
    filename= r.url[c.rfind('/')+1:]

    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=10000):
            f.write(chunk)
        print("Downloaded !")
    
else:
    print("Please run the program again and choose from the correct options !!")
