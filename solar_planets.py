import cv2
import numpy

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (100, 90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (20, 70, 200)
            )

cv2.putText(img,
            "Mercury",
            (130, 238),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (194, 260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.43,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (289, 263),
            cv2.FONT_HERSHEY_COMPLEX,
            0.43,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (385, 255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.43,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (550, 390),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (780, 330),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (970, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.57,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1115, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.53,
            (255,255,255)
            )

cv2.imshow("Output :", img)
cv2.waitKey(0)
