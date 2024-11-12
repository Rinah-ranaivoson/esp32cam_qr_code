import cv2
import urllib.request
import numpy as np
from pyzbar.pyzbar import decode

# Replace the URL with your ESP32Cam video stream URL
url = 'http://192.168.137.244/cam-hi.jpg'

# Window name
window_name = 'ESP32Cam QR Code Decoder'

# Create a window to display the image
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

while True:
    # Read the video stream from the ESP32Cam
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    
    # Decode the image using OpenCV
    frame = cv2.imdecode(imgnp, -1)

    # If the image is successfully retrieved
    if frame is not None:
        # Decode the QR codes in the image
        for d in decode(frame):
            s = d.data.decode()  # Decode the content of the QR code
            print(s)  # Print the QR code content to the console
            
            # Draw a rectangle around the QR code
            frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                  (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
            
            # Add the QR code text next to it
            frame = cv2.putText(frame, s, (d.rect.left, d.rect.top + d.rect.height),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the image with the detected QR code
        cv2.imshow(window_name, frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the window and release resources
cv2.destroyWindow(window_name)
