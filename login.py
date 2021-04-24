#!C:\Users\aravi\AppData\Local\Programs\Python\Python39\python.exe
import cgi
from base64 import b64decode
import face_recognition
#import webbrowser

formData = cgi.FieldStorage()
face_match=0

image=formData.getvalue("current_image")
email=formData.getvalue("email")
data_uri = image
header, encoded = data_uri.split(",", 1)
data = b64decode(encoded)

with open("image.png", "wb") as f:
    f.write(data)

got_image = face_recognition.load_image_file("image.png")

try:

    existing_image = face_recognition.load_image_file("students/"+email+".jpg")

    got_image_facialfeatures = face_recognition.face_encodings(got_image)[0]

    existing_image_facialfeatures = face_recognition.face_encodings(existing_image)[0]

    results= face_recognition.compare_faces([existing_image_facialfeatures],got_image_facialfeatures)

    if(results[0]):
        face_match=1
    else:
        face_match=0

    print("Content-Type: text/html")
    print()

    if(face_match==1):
        #print("<script>alert('Welcome ",email," ')</script>")
        print("<script>location.replace('loginSuccess.html')</script>")
    else:
        #print("<script>alert('Face is not recognized/exist in database')</script>")
        print("<script>location.replace('faceNotRecognized.html')</script>")

except(FileNotFoundError):
    print("Content-Type: text/html")
    print()
    #print("<script>alert('Email ID not found')</script>")
    print("<script>location.replace('idNotFound.html')</script>")


except(IndexError):
    print("Content-Type: text/html")
    print()
    #print("<script>alert('Captured image is not a proper face')</script>")
    print("<script>location.replace('notProperFace.html')</script>")
