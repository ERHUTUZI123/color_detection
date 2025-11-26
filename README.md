# Color Detection
Color Detection can frame the object with a specific color using a green bounding box.

Open your IDE and terminal, enter 
```
gh repo clone ERHUTUZI123/color_detection
```
to clone.

Make sure you install ```python``` and ```pip```, then enter ```pip install -r requirements.txt``` to install all required packages.

Get your target color BGR (Blue, Green, Red) values, replace ```color = [0, 255, 255]``` with them. By default it is yellow.

Run ```main.py```.

If no window pops up and terminal outputs ```Failed to grab frame```, try to change ```cap = cv2.VideoCapture(0)``` to ```cap = cv2.VideoCapture(1)``` or ```cap = cv2.VideoCapture(2)```.

Happy detecting!
