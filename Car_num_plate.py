import cv2

#######################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier(r"C:\Users\PRATEEK\Desktop\hackathon\haarcascade_russian_plate_number.xml")
minArea=500
color = (255,0,255)
#######################################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


while True:
    succ, img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area >minArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break