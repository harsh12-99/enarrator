from flask import Flask,send_from_directory
from flask import request,redirect,render_template,url_for
from werkzeug.utils import secure_filename
from googletrans import Translator 
from gtts import gTTS
import os
import pytesseract
from PIL import ImageFilter
from PIL import Image
import playsound
import uuid
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './media'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#Function to convert image to text.
@app.route('/submitImage',methods=['POST', 'GET'])
def submitImage():
    image = request.files['ocrImage']
    text = ''
    filename = (image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    text = pytesseract.image_to_string(img,lang='eng')
    f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename)+'.txt','w')
    f.write(text)
    fn = texttoaudio(text)
#    fn2 = translate(text)
    f.close()
    return render_template('output.html',text=text,filename=fn)

# def translate(t):
#     p = Translator()
#     k = p.translate(t, dest = 'hindi')
#     return k

#Function to convert text to speech
#This will return filename and save the audio file in audio folder
def texttoaudio(t):
    tts = gTTS(text=t, lang='en')
    filename = "./audio/"+str(uuid.uuid1())+".mp3"
    tts.save(filename)
    return filename

#This function will send the audio file to the audio player on home page
@app.route('/music/<path:filename>',methods=['POST','GET'])
def download_file(filename):
    return send_from_directory('./', filename)

if __name__ == '__main__':
    app.run(debug=True)
    #'0.0.0.0',8000