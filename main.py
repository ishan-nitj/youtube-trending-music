from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template,request

app=Flask(__name__)

def getdata(url):#top music videos of all time
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
    #print (videolinks[0])
    return imagelinks,titles,videolinks #return a tuple

all_time=getdata("https://www.youtube.com/playlist?list=PLFgquLnL59amLh5g4ZZoSl1Wf9e0_rco7")
pop=getdata("https://www.youtube.com/playlist?list=PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ")
electronic=getdata("https://www.youtube.com/playlist?list=PLFPg_IUxqnZNnACUGsfn50DySIOVSkiKI")
house_music=getdata("https://www.youtube.com/playlist?list=PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ")
edm=getdata("https://www.youtube.com/playlist?list=PLUg_BxrbJNY5gHrKsCsyon6vgJhxs72AH")
pop_rock=getdata("https://www.youtube.com/playlist?list=PLr8RdoI29cXIlkmTAQDgOuwBhDh3yJDBQ")
hip_hop=getdata("https://www.youtube.com/playlist?list=PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo")
rock=getdata("https://www.youtube.com/playlist?list=PLhd1HyMTk3f5PzRjJzmzH7kkxjfdVoPPj")

list_of_tuples=[]
list_of_tuples.append(all_time)
list_of_tuples.append(electronic)
list_of_tuples.append(edm)
list_of_tuples.append(pop_rock)
list_of_tuples.append(rock)
list_of_tuples.append(pop)
list_of_tuples.append(house_music)
list_of_tuples.append(hip_hop)

display_names=[]
display_names.append("ALL TIME")
display_names.append("ELECTRONIC")
display_names.append("EDM")
display_names.append("POP ROCK")
display_names.append("ROCK")
display_names.append("POP")
display_names.append("HOUSE MUSIC")
display_names.append("HIP HOP")

@app.route('/')
def index():
    return render_template("home.html",list_of_tuples=list_of_tuples,display_names=display_names)

if __name__=="__main__": 
    app.run(debug=True)

    
