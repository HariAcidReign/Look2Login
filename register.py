#!C:\Users\aravi\AppData\Local\Programs\Python\Python39\python.exe
from pathlib import Path
import cgi
from base64 import b64decode
import face_recognition

formData = cgi.FieldStorage()
face_match = 0

image = formData.getvalue("current_image")
email = formData.getvalue("email")
data_uri = image
header, encoded = data_uri.split(",", 1)
data = b64decode(encoded)

with open("image.png", "wb") as f:
    f.write(data)

got_image = face_recognition.load_image_file("image.png")

try:
    got_image_facialfeatures = face_recognition.face_encodings(got_image)[0]
    existing_image = face_recognition.load_image_file("students/"+email+".jpg")
    print("Content-Type: text/html")
    print()
    print(email)
    #print("<script>alert('Email ID already exist')</script>")
    print("<script>location.replace('errorDuplicateID.html')</script>")

except(IndexError):
    print("Content-Type: text/html")
    print()
    # print("<script>alert('Captured image is not a proper face')</script>")
    print("<script>location.replace('notProperFace.html')</script>")

except(FileNotFoundError):
    print("Content-Type: text/html")
    print()
    path_file_name = './students/'+email+'.jpg'
    Path(path_file_name).touch()
    with open(path_file_name, "wb") as f:
        f.write(data)
    # print("<script>alert('Credentials added successfully')</script>")
    print("<script>location.replace('registerSuccessful.html')</script>")



