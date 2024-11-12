Voici un fichier README pour votre code, expliquant son fonctionnement et comment l'utiliser :

---

# ESP32Cam QR Code Decoder

This project allows you to capture video from an ESP32Cam and decode QR codes in real-time. The ESP32Cam stream is fetched via HTTP, and any QR codes present in the stream are detected and decoded using the `pyzbar` library. The decoded content is displayed on the video feed, along with a green rectangle around the detected QR code.

## Requirements

Before running the script, you need to have the following libraries installed:

1. **OpenCV** for image processing and displaying the video feed.
2. **NumPy** for handling image arrays.
3. **pyzbar** for decoding QR codes from the image frames.

You can install the required dependencies using `pip`:

```bash
pip install opencv-python numpy pyzbar
```

## Setup

### ESP32Cam Stream URL

To use this script with your own ESP32Cam, you need to replace the stream URL with the URL provided by your ESP32Cam. 

Typically, the ESP32Cam might provide a stream URL like this:
```
http://<ESP32_IP_ADDRESS>/cam-hi.jpg
```
Where `<ESP32_IP_ADDRESS>` is the IP address of your ESP32Cam device.

Make sure that your ESP32Cam is connected to the same network as the machine running this script.

### Running the Script

1. **Set the ESP32Cam URL**:
   In the script, locate the following line and replace the URL with your ESP32Cam stream URL:
   ```python
   url = 'http://192.168.137.244/cam-hi.jpg'
   ```

2. **Run the Script**:
   Execute the script in your terminal or Python environment:
   ```bash
   python esp32cam_qr_decoder.py
   ```

3. **QR Code Detection**:
   - The video feed will be displayed in a window called **"ESP32Cam QR Code Decoder"**.
   - If any QR code is detected in the image frame, it will display a green rectangle around the QR code and the decoded content will be shown next to the QR code.
   - The decoded QR code content will also be printed to the terminal.

4. **Exit the Application**:
   - To stop the script and close the video window, press the **`q`** key.

## Notes

- **ESP32Cam Stream**: This script assumes the ESP32Cam provides a static JPEG image at the given URL. If you are using a different type of video stream (e.g., MJPEG), the method to retrieve and decode the stream may need to be adjusted.
- **Latency**: If you experience delays in detecting the QR codes, it may be due to the time taken to fetch and decode each image. Using a faster camera stream or optimizing the stream quality can help reduce latency.
- **Error Handling**: Ensure that the ESP32Cam stream is accessible over your network. If the connection fails, the script will not be able to retrieve frames.

## Example Output

- QR code detected:
  ```
  1234567890abcdef
  ```
- Image display: The video feed will show a rectangle around any detected QR code and display the decoded text near the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the content based on any specific requirements or changes you make to the code.
