import pytube
from flask import Flask,redirect, url_for,render_template,request
import requests, random
requests.packages.urllib3.disable_warnings()
import ssl 

path='C:/Users/Win10/Desktop/GOGO Downloads'

app=Flask(__name__)

def fun(video_url,path):
	youtube = pytube.YouTube(video_url)
	video = youtube.streams.first()
	video.download(path)


@app.route('/')
def renderHomePage():
    return render_template("upload.html")

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['url']
	
	if text == "":
		
		return render_template('upload.html' , eval=1)
	
	if text== "qwerty":
		return render_template('upload.html' , eval=3)	
		
	else:
		fun(text,path)
		return render_template('upload.html' , eval=2)
	

if __name__== '__main__':
    app.run(debug='true')



