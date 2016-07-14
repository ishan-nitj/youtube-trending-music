from bs4 import BeautifulSoup
import requests
from threading  import Thread
from flask import Flask,render_template,request
import time

app=Flask(__name__)

list_of_tuples=[]
display_names=[]

def getdata(url,no):#top music videos of all time
    print "Thread %s started at "%(no)+str(time.ctime(time.time()))+"\n"
    r=requests.get(url)
    data=r.text
    soup=BeautifulSoup(data)
    #Images
    images=soup.select(".yt-thumb-clip")
    imagelinks=[]#A list of size 100 containing the link to all 100 images
    for image in images[9:len(images)]:#First few images are useless
            imagelinks.append(image.img["data-thumb"])
    #Titles and Videolinks
    links=soup.find_all("a",class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link ",limit=10)
    titles=[] #A list of size 100 containing titles of all 100 songs
    videolinks=[]#A list of size 100 containing links to all videos
    for link in links:
        titles.append(link.string.strip())
        videolinks.append("https://youtube.com"+link["href"])
    datatuple=imagelinks,titles,videolinks #make a tuple
    list_of_tuples.append(datatuple)
    print "Thread %s completed at "%(no)+str(time.ctime(time.time()))+"\n"
    
def Main():
    t1=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLFgquLnL59amLh5g4ZZoSl1Wf9e0_rco7",1))
    t2=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ",2))
    t3=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLFPg_IUxqnZNnACUGsfn50DySIOVSkiKI",3))
    t4=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ",4))
    t5=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLUg_BxrbJNY5gHrKsCsyon6vgJhxs72AH",5))
    t6=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLr8RdoI29cXIlkmTAQDgOuwBhDh3yJDBQ",6))
    t7=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo",7))
    t8=Thread(target=getdata,args=("https://www.youtube.com/playlist?list=PLhd1HyMTk3f5PzRjJzmzH7kkxjfdVoPPj",8))
    display_names.append("ALL TIME")
    display_names.append("ELECTRONIC")
    display_names.append("EDM")
    display_names.append("POP ROCK")
    display_names.append("ROCK")
    display_names.append("POP")
    display_names.append("HOUSE MUSIC")
    display_names.append("HIP HOP")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()	
    
Main()

print "Main Thread started at "+str(time.ctime(time.time()))
    
@app.route('/')
def index():
    return render_template("home.html",list_of_tuples=list_of_tuples,display_names=display_names)

if __name__=="__main__": 
    app.run(debug=False)

    
