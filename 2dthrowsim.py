import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


webcam = cv2.VideoCapture(0)

low_green = np.array([25, 52, 72])

high_green = np.array([102, 255, 255])

LowerP = 1000
HigherP = 6000

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []
def animate(i):
    plt.plot(xs, ys, color = "red")
while True:
    cam, frame = webcam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imask = cv2.inRange(hsv, low_green, high_green)

    (countourFind,_) = cv2.findContours(imask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in countourFind:
        area = cv2.contourArea(countour)

        if area < LowerP or area > HigherP:
            continue
        (x, y, width, height) = cv2.boundingRect(countour)

        rect = cv2.rectangle(frame, (x,y), (x+width, y+height), (255, 0, 0), 3)
        global cx
        global cy
        cx = int((width/2) + x)
        cy = int((height/2) + y)
        c = (cx, cy)
        xs.append(cx)
        ys.append(cy)
        cv2.putText(rect, "Tennis ball", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (366, 255, 12), 2)
    cv2.imshow("Normal vid", frame)

    key = cv2.waitKey(1)
    if (key == ord("q")):
            break


plt.gca().invert_yaxis()

ani = animation.FuncAnimation(fig, animate, frames = 50, interval = 1000)

plt.show()

webcam.release()
cv2.destroyAllWindows()
