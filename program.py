import cv2 as cv
print(cv.__version__)

original_image = cv.imread("image.jpg")
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.3)

print(detected_faces) # human faces identified

for(column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

small = cv.resize(original_image, (0, 0), fx=0.3, fy=0.3)
cv.imshow('Image', small)
cv.waitKey(0)
cv.destroyAllWindows()


