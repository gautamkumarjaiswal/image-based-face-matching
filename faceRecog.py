import face_recognition


known_image = face_recognition.load_image_file("PersonA1.png") #change image file

#imgplot = plt.imshow(known_image)
#plt.show()

unknown_image = face_recognition.load_image_file("PersonB3.jpg") #change image file
#imgplot = plt.imshow(unknown_image)
#plt.show()

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face,
#I only care about the first encoding in each image, so I grab index 0.


biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

print(results)

if results == [True]:
    print("Both images are of the same person")
else:
    print("Two images are of two different persons")
