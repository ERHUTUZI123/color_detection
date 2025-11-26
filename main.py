import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    if not ret or frame is None:
        print("Failed to grab frame")
        break

    cv2.imshow('fram', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv2.destroyAllWindows()