from flask import Flask,render_template,request,session,flash,redirect
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import os
import cv2
from keras.models import load_model,model_from_json
import numpy as np
import aspose.threed as a3d

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/')
ALLOWED_EXTENSIONS = {'jfif', 'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.secret_key = 'sameer'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict',  methods=['POST', 'GET'])
def uploadFile():
    if request.method == 'POST':
        if 'uploaded-file' not in request.files:
            return render_template('index.html')
        uploaded_img = request.files['uploaded-file']
        if uploaded_img.filename == '':
            return render_template('index.html')
        uploaded_img.save('static/file.jpg')
        img1 = cv2.imread('static/file.jpg')
        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        #cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
        faces = cascade.detectMultiScale(gray, 1.1, 3)
        for x,y,w,h in faces:
            cv2.rectangle(img1, (x,y), (x+w, y+h), (0,255,0), 2)
            cropped = img1[y:y+h, x:x+w]
        cv2.imwrite('static/after.jpg', img1)
        try:
            cv2.imwrite('static/cropped.jpg', cropped)
        except:
            pass
        try:
            image = cv2.imread('static/cropped.jpg', 0)
        except:
            image = cv2.imread('static/file.jpg', 0)
        image = cv2.resize(image, (48,48))
        image = image/255.0
        image = np.reshape(image, (1,48,48,1))
        model = model_from_json(open("emotion_model1.json", "r").read())
        model.load_weights('model.h5')
        prediction = model.predict(image)
        label_dict = {0:'Angry',1:'Disgust',2:'Fear',3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}
        prediction = list(prediction[0])
        img_index = prediction.index(max(prediction))
        final_prediction=label_dict[img_index]
        return render_template('predict.html', data=final_prediction)

#scene=a3d.Scene.from_file("static/mesh0.obj")
#scene.save("static/result.glTF")

@app.route('/contact')
def main2():
    return render_template('contact.html')

@app.route('/about')
def main3():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)